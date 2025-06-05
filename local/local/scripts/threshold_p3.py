import telnetlib
import time

# Telnet server details
host = "0.0.0.0"
port = 8086
timeout = 1
sps = 1

# Commands to send
attack0 = b"pipeline PIPELINE1 regrd attack index 0\n"
proto0 = b"pipeline PIPELINE1 regrd proto_0 index 0\n"
syn_count0= b"pipeline PIPELINE1 regrd syn_flood_syn_counts_reg index 0\n"
syn_flood1= b"pipeline PIPELINE1 regwr syn_flood_syn_flood_reg value 1 index 0\n"
syn_flood0= b"pipeline PIPELINE1 regwr syn_flood_syn_flood_reg value 0 index 0\n"

k = 4
# last_k = [0] * k

last_k = []

# Function to connect to telnet server and send command
def telnet_session(host, port, timeout):
    try:
        # Connect to the telnet server
        tn = telnetlib.Telnet(host, port, timeout)
        tn.read_until(b"Escape character is", timeout)

        tn.write(attack0)
        output = tn.read_until(b"\n", timeout)
        tn.write(syn_count0)
        output = tn.read_until(b"\n", timeout)
        string_output = output.decode('utf-8')
        syn_count0_hex = string_output.split(' ')[1].strip()
        syn_count0_dec_prev = int(syn_count0_hex, 16)
        
        cap = 0
        first_k = False
        prediction = False
        a = 0.2
        skip_k = 0
        flood = False
        syn_persec_pred = 0

        lower_bound_allow = 10000

        margin_on_error = 1.2

        with open("output.txt", "w") as file:
            while True:
                try:
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
                    
                    hold = False
                    allow_count = 4000000000
                    cap += 1

                    syn_count0_dec_diff = syn_count0_dec - syn_count0_dec_prev
                    syn_count0_dec_prev = syn_count0_dec
                    if(len(last_k)<k):
                        last_k.append(syn_count0_dec_diff)
                    # last_k.pop(0)
                    # last_k.append(syn_count0_dec_diff)
                    # print(last_k)
                    # syn_count0_dec_prev = syn_count0_dec


                    elif (prediction == False): # i have 10 numerical values
                        first_k = True
                        deltas = [last_k[i+1] - last_k[i] for i in range(k - 1)]
                        # deltas_abs = [abs(deltas[i]) for i in range(len(deltas))]
                        average_delta= sum(deltas) / len(deltas)

                        syn_persec_exp = last_k[-1] + average_delta
                        prediction = True
                        # continue

                            # print("All elements are non-zero.", cap, first_k)
                    # else: 
                    #     first_k = False
                    #     prediction = False

                    else: 
                        print("predicted:",syn_persec_exp,"VS. actual:",syn_count0_dec_diff)
                        allow_count = max(margin_on_error*syn_persec_exp,lower_bound_allow)
                        e_ratio = syn_persec_exp / syn_count0_dec_diff if syn_count0_dec_diff != 0 else float('inf')
                        # e_diff = last_k[-1] - syn_persec_pred
                        a1 = 1 - a
                        a2 = 1 + a
                        # if (e_ratio<a1 or e_ratio>a2):
                        if (e_ratio<a1):
                            flood = True
                            print("!!! FLOOD ALERT !!!")
                            first_k = False
                        elif(flood == True):
                            margin_on_error = 1.4
                            last_k.pop(0)
                            last_k.append(syn_count0_dec_diff)
                            print(last_k)
                            syn_count0_dec_prev = syn_count0_dec
                            flood = False
                        else:
                            margin_on_error = 1.2
                            last_k.pop(0)
                            last_k.append(syn_count0_dec_diff)
                            print(last_k)
                            syn_count0_dec_prev = syn_count0_dec

                            deltas = [last_k[i+1] - last_k[i] for i in range(k - 1)]
                            average_delta= sum(deltas) / len(deltas)
                            syn_persec_exp = (last_k[-1] + average_delta) if (last_k[-1] + average_delta) > 0 else 0

                            flood = False

                        print("------------- alpha:", a, "range:",a1,a2, "ratio:", e_ratio)

                    # else: # skip for the first set of values
                    #     if skip_k > 0:
                    #         skip_k = skip_k -1
                    #         first_k = False
                    #     print("no prediction", skip_k)
                            
                    # if first_k == True: # compute expected value
                    #     deltas = [last_k[i+1] - last_k[i] for i in range(k - 1)]
                    #     # deltas_abs = [abs(deltas[i]) for i in range(len(deltas))]
                    #     average_delta= sum(deltas) / len(deltas)
                    #     print(deltas, average_delta)

                    #     syn_persec_exp = last_k[-1] + average_delta
                    #     if syn_persec_exp < 0: # correction
                    #         syn_persec_exp = 0
                        
                    #     if syn_persec_pred == 0: # initial expectation
                    #         syn_persec_pred = syn_persec_exp
                    #         prediction = True
                    #         print("initial expected:",syn_persec_exp)
                    #     else:
                            
                    #         ratio = syn_persec_exp / syn_persec_pred
                    #         betta = 0.3
                    #         if (ratio>1-betta and ratio<1+betta):
                    #             syn_persec_pred = syn_persec_exp
                    #             prediction = True
                    #             print("expected:",syn_persec_exp)
                    #         else:
                    #             # flood = True
                    #             # skip_k = 3
                    #             # first_k = False
                    #             hold = True
                    #             print("skip expectation")

                    # if (flood == True and average_delta<0): # correction
                    #     flood = False
                    # if (hold == True):
                    #     flood = True
                    # if flood == True:
                    #         drop_percent = ( 1- e_ratio ) * 100
                    #         if (drop_percent < 0 or hold == True): # correction
                    #             drop_percent = 0
                    #         print("!!! FLOOD ALERT !!!" , 'drop', drop_percent,"%")
                    #         tn.write(syn_flood1)
                    #         output = tn.read_until(b"\n", timeout)          
                    # else:
                    #     drop_percent = 0
                    #     print("normal behavior" , 'drop', drop_percent,"%")
                    #     tn.write(syn_flood0)
                    #     output = tn.read_until(b"\n", timeout)
                    #     # pipeline PIPELINE1 regrd syn_flood_syn_flood_reg index 0

                    print("allowed:", allow_count)
                    drop_command = f"pipeline PIPELINE1 regwr syn_flood_allow_count_reg value {int(allow_count)} index 0\n"
                    tn.write(drop_command.encode())
                    output = tn.read_until(b"\n", timeout)
                    
                    
                    tn.write(b"pipeline PIPELINE1 regwr syn_flood_syn_percent_iterator_reg value 0 index 0\n")
                    output = tn.read_until(b"\n", timeout)
                    # pipeline PIPELINE1 regrd syn_flood_syn_drop_percent_reg index 0

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