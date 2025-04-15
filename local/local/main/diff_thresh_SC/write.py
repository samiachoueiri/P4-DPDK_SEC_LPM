import telnetlib
import time

# Telnet server details
host = "0.0.0.0"
port = 8086
timeout = 1
sps = 1

# Commands to send
syn_count0= b"pipeline PIPELINE0 regrd syn_flood_syn_counts_reg index 0\n"
syn_flood1= b"pipeline PIPELINE0 regwr syn_flood_syn_flood_reg value 1 index 0\n"
syn_flood0= b"pipeline PIPELINE0 regwr syn_flood_syn_flood_reg value 0 index 0\n"

# Function to connect to telnet server and send command
def telnet_session(host, port, timeout):
    try:
        # Connect to the telnet server
        tn = telnetlib.Telnet(host, port, timeout)
        tn.read_until(b"Escape character is", timeout)

        tn.write(syn_count0)
        output = tn.read_until(b"\n", timeout)
        string_output = output.decode('utf-8')
        # syn_count0_hex = string_output.split(' ')[1].strip()
        syn_count0_hex = string_output
        syn_count0_dec = int(syn_count0_hex, 16)

        cap = 0

        while True:
            try:
                tn.write(syn_count0)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                syn_count0_hex = string_output.split(' ')[1].strip()
                syn_count0_dec = int(syn_count0_hex, 16)
                print("count:","P0",syn_count0_dec,"iter",cap)
                                
                if (cap > 20):
                    var = int(5)
                    command = f"pipeline PIPELINE0 regwr syn_flood_syn_flood_reg value {var} index 0\n"
                    tn.write(command.encode())
                    output = tn.read_until(b"\n", timeout)
                    string_output = output.decode('utf-8')
                    syn_flood1_hex = string_output.split(' ')[1].strip()
                    syn_flood1_dec = int(syn_flood1_hex, 16)
                    # pipeline PIPELINE0 regrd syn_flood_syn_flood_reg index 0
                else:
                    tn.write(syn_flood0)
                    output = tn.read_until(b"\n", timeout)
                    string_output = output.decode('utf-8')
                    syn_flood0_hex = string_output.split(' ')[1].strip()
                    syn_flood0_dec = int(syn_flood0_hex, 16)
                cap += 1
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