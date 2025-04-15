import telnetlib
import time

# Telnet server details
host = "0.0.0.0"
port = 8086
timeout = 1
sps = 1

# Command to send
get_index = b"pipeline PIPELINE0 regrd reg_index_0 index 0\n"
# get_index = b"pipeline PIPELINE0 regrd ht0_0 index 0x5226\n"
#0x4270
# Function to connect to telnet server and send command
def telnet_session(host, port, timeout):
    try:
        # Connect to the telnet server
        tn = telnetlib.Telnet(host, port, timeout)
        tn.read_until(b"Escape character is", timeout)

        tn.write(get_index)
        output = tn.read_until(b"\n", timeout)
        
        while True:
            try:
                # tn.write(get_index)
                # output = tn.read_until(b"\n", timeout)
                # string_output = output.decode('utf-8')
                # index_hex = string_output.split(' ')[1].strip()
                # index_dec = int(index_hex, 16)
                index_hex = '0x4270'
                
                get_last = f"pipeline PIPELINE0 regrd reg_last_0 index {index_hex}\n"
                get_last = get_last.encode('utf-8')
                tn.write(get_last)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                last_hex = string_output.split(' ')[1]
                last_dec = int(last_hex, 16)

                get_curr = f"pipeline PIPELINE0 regrd reg_curr_0 index {index_hex}\n"
                get_curr = get_curr.encode('utf-8')
                tn.write(get_curr)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                curr_hex = string_output.split(' ')[1]
                curr_dec = int(curr_hex, 16)

                get_count = f"pipeline PIPELINE0 regrd ht0_0 index {index_hex}\n"
                get_count = get_count.encode('utf-8')
                tn.write(get_count)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                count_hex = string_output.split(' ')[1]
                count_dec = int(count_hex, 16)

                get_iat = f"pipeline PIPELINE0 regrd reg_iat_0 index {index_hex}\n"
                # get_iat = f"pipeline PIPELINE0 regrd reg_test_0 index 0\n"
                get_iat = get_iat.encode('utf-8')
                tn.write(get_iat)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                iat_hex = string_output.split(' ')[1]
                iat_dec = int(iat_hex, 16)
                
                print("flow:",index_hex,"pkt count:",count_dec,"Last:",last_dec,"Curr:",curr_dec,"IAT:",iat_dec)
                time.sleep(1/sps)  # Adjust as needed to control frequency of command sending
            
            except KeyboardInterrupt:
                print("\nProcess interrupted. Closing...")
                break  # Exit the loop on interrupt

    except Exception as e:
        print(f"Error: {e}")

    finally:
        tn.close()  # Ensure tn.close() is executed

# Start the telnet session
telnet_session(host, port, timeout)
