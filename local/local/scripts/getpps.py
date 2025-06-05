import telnetlib
import time

# Telnet server details
host = "0.0.0.0"
port = 8086
timeout = 1
sps = 10

# Commands to send
attack0 = b"pipeline PIPELINE0 regrd attack index 0\n"
proto0 = b"pipeline PIPELINE0 regrd proto_0 index 0\n"
time0= b"pipeline PIPELINE0 regrd syn_flood_reg_time index 0\n"
time_diff0= b"pipeline PIPELINE0 regrd syn_flood_reg_time_diff index 0\n"
k = 10
last_k = [0] * k


# Function to connect to telnet server and send command
def telnet_session(host, port, timeout):
    try:
        # Connect to the telnet server
        tn = telnetlib.Telnet(host, port, timeout)
        tn.read_until(b"Escape character is", timeout)

        tn.write(attack0)
        output = tn.read_until(b"\n", timeout)
        tn.write(time0)
        output = tn.read_until(b"\n", timeout)
        string_output = output.decode('utf-8')
        time0_hex = string_output.split(' ')[1].strip()
        # time0_dec_prev = int(time0_hex, 16)

        cap = 0
        # first_k = False
        # prediction = False
        # a = 0.5
        # skip_k = 0
        # flood = False
        
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
                    tn.write(time0)
                    output = tn.read_until(b"\n", timeout)
                    string_output = output.decode('utf-8')
                    time0_hex = string_output.split(' ')[1].strip()
                    time0_dec = int(time0_hex, 16)

                    tn.write(time_diff0)
                    output = tn.read_until(b"\n", timeout)
                    string_output = output.decode('utf-8')
                    time_diff0_hex = string_output.split(' ')[1].strip()
                    time_diff0_dec = int(time_diff0_hex, 16)

                    cap = cap + 1
                    print("proto:","P0",proto0_hex, "attack:","P0",attack0_hex,"i",cap)
                    print("time",time0_dec, "diff",time_diff0_dec)

                    # syn_count0_dec_diff = syn_count0_dec - syn_count0_dec_prev
                    # last_k.pop(0)
                    # last_k.append(syn_count0_dec_diff)
                    # print(last_k)
                    # syn_count0_dec_prev = syn_count0_dec
                    # cap += 1

                    # if 0 not in last_k: # i have 10 numerical values
                    #     if cap >= k:
                    #         first_k = True
                    #         # print("All elements are non-zero.", cap, first_k)
                    # else: 
                    #     first_k = False
                    #     prediction = False

                    # if prediction == True and skip_k == 0: 
                    #     print("predicted:",syn_persec_exp,"VS. actual:",last_k[-1])
                    #     e_ratio = syn_persec_exp / last_k[-1] if last_k[-1] != 0 else float('inf')
                    #     # e_diff = last_k[-1] - syn_persec_exp
                    #     a1 = 1 - a
                    #     a2 = 1 + a
                    #     # if (e_ratio<a1 or e_ratio>a2):
                    #     if (e_ratio<a1):
                    #         flood = True
                    #         skip_k = k
                    #     else:
                    #         flood = False

                    #     print("------------- alpha:", a, "range:",a1,a2, "ratio:", e_ratio)

                    # else: # skip for the first set of values
                    #     if skip_k > 0:
                    #         skip_k = skip_k -1
                    #     print("no prediction", skip_k)
                            
                    # if first_k == True: # compute expected value
                    #     deltas = [last_k[i+1] - last_k[i] for i in range(k - 1)]
                    #     # deltas_abs = [abs(deltas[i]) for i in range(len(deltas))]
                    #     average_delta= sum(deltas) / len(deltas)
                    #     print(deltas, average_delta)

                    #     syn_persec_exp = last_k[-1] + average_delta
                    #     if syn_persec_exp < 0:
                    #         syn_persec_exp = 0
                    #     print("expected:",syn_persec_exp)
                    #     prediction = True

                    # # problem: i am adding delta (tp) to total count, also i need to check if i am considering the appended (new, current) value
                    # # mainly i need to compare the predition with the last_k[-1]
                    # if flood == True:
                    #     if average_delta < 0:
                    #         flood = False
                    #     else:
                    #         print("!!! FLOOD ALERT !!!")
                    
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
