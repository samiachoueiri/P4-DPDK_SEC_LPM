import telnetlib
import time

# Telnet server details
host = "0.0.0.0"
port = 8086
timeout = 1
sps = 1

# Commands to send
attack0 = b"pipeline PIPELINE0 regrd attack index 0\n"
proto0 = b"pipeline PIPELINE0 regrd proto_0 index 0\n"
syn_count0= b"pipeline PIPELINE0 regrd syn_flood_syn_counts_reg index 0\n"
syn_flood1= b"pipeline PIPELINE0 regwr syn_flood_syn_flood_reg value 1 index 0\n"
syn_flood0= b"pipeline PIPELINE0 regwr syn_flood_syn_flood_reg value 0 index 0\n"

k = 4
last_k = []

# Function to connect to telnet server and send command
def telnet_session(host, port, timeout):
    try:
        # Connect to the telnet server
        tn = telnetlib.Telnet(host, port, timeout)
        tn.read_until(b"Escape character is", timeout)

#grab first sample
        tn.write(attack0)
        output = tn.read_until(b"\n", timeout)
        tn.write(syn_count0)
        output = tn.read_until(b"\n", timeout)
        string_output = output.decode('utf-8')
        syn_count0_hex = string_output.split(' ')[1].strip()
        syn_count0_dec_prev = int(syn_count0_hex, 16)

#constants
        cap = -(k+2)
        prediction = False
        a = 0.5 #0.2
        flood = False
        lower_bound_allow = 10000 #allow at least 10000 pkts per sec
        margin_on_error = 1+a #allow 20% more pkts

        with open("output.txt", "w") as file:
            while True:
                try:
#grab sample
                    cap +=1
                    tn.write(proto0)
                    output = tn.read_until(b"\n", timeout)
                    string_output = output.decode('utf-8')
                    proto0_hex = string_output.split(' ')[1].strip()
                    tn.write(attack0)
                    output = tn.read_until(b"\n", timeout)
                    string_output = output.decode('utf-8')
                    attack0_hex = string_output.split(' ')[1].strip()
                    tn.write(syn_count0)
                    output = tn.read_until(b"\n", timeout)
                    string_output = output.decode('utf-8')
                    syn_count0_hex = string_output.split(' ')[1].strip()
                    syn_count0_dec = int(syn_count0_hex, 16)
                    print("proto:","P0",proto0_hex, "attack:","P0",attack0_hex,"count:","P0",syn_count0_dec,"iter",cap)

#reset allow_count to high value 
                    allow_count = 4000000000

#calculate count per sec (number of syn pkts in the last sec)
                    syn_count0_dec_diff = syn_count0_dec - syn_count0_dec_prev
                    syn_count0_dec_prev = syn_count0_dec

#fill the array Y with k elements 
                    if(len(last_k)<k):
                        last_k.append(syn_count0_dec_diff)
#we have k elements, get first prediction
                    elif (len(last_k)==k and prediction == False):
                        last_k.pop(0)
                        last_k.append(syn_count0_dec_diff)
                        deltas = [last_k[i+1] - last_k[i] for i in range(k - 1)]
                        average_delta= sum(deltas) / len(deltas)
                        syn_persec_exp = last_k[-1] + average_delta
                        prediction = True
                    else: 
                        print("predicted:",syn_persec_exp,"VS. actual:",syn_count0_dec_diff)
                        allow_count = max(margin_on_error*syn_persec_exp,lower_bound_allow)
                        e_ratio = syn_persec_exp / syn_count0_dec_diff if syn_count0_dec_diff != 0 else float('inf')
                        a1 = 1 - a
                        a2 = 1 + a
                        file.write(f"{cap} {a} {k} {syn_count0_dec_diff} {syn_persec_exp} {allow_count} {e_ratio} \n")
                        # if (e_ratio<a1 or e_ratio>a2):
                        if (e_ratio<a1):
                            flood = True
                            print("!!! FLOOD ALERT !!!")
                        elif(flood == True):
                            margin_on_error = 1+(2*a)
                            last_k.pop(0)
                            last_k.append(syn_count0_dec_diff)
                            print(last_k)
                            syn_count0_dec_prev = syn_count0_dec
                            flood = False
                        else:
                            margin_on_error = 1+a
                            last_k.pop(0)
                            last_k.append(syn_count0_dec_diff)
                            print(last_k)
                            syn_count0_dec_prev = syn_count0_dec

                            deltas = [last_k[i+1] - last_k[i] for i in range(k - 1)]
                            average_delta= sum(deltas) / len(deltas)
                            syn_persec_exp = (last_k[-1] + average_delta) if (last_k[-1] + average_delta) > 0 else 0

                            flood = False

                        print("------------- alpha:", a, "range:",a1,a2, "ratio:", e_ratio)

                    print("allowed:", allow_count)
                    drop_command = f"pipeline PIPELINE0 regwr syn_flood_allow_count_reg value {int(allow_count)} index 0\n"
                    tn.write(drop_command.encode())
                    output = tn.read_until(b"\n", timeout)
                    
                    
                    tn.write(b"pipeline PIPELINE0 regwr syn_flood_syn_percent_iterator_reg value 0 index 0\n")
                    output = tn.read_until(b"\n", timeout)
                    # pipeline PIPELINE0 regrd syn_flood_syn_drop_percent_reg index 0
                    print("++++++++++++++++++++++++++++++++++++++++++++++++")
                    time.sleep(1/sps)
                
                except KeyboardInterrupt:
                    print("\nProcess interrupted. Closing...")
                    break  # Exit the loop on interrupt

    except Exception as e:
        print(f"Error: {e}")

    finally:
        tn.close()  # Ensure tn.close() is executed

# Start the telnet session
telnet_session(host, port, timeout)