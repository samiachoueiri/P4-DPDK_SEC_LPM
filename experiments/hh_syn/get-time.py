import telnetlib
import time

# Telnet server details
host = "0.0.0.0"
port = 8086
timeout = 1

# Command to send
command = b"pipeline PIPELINE0 regwr syn_counts_reg_0 value 0 index 0\n"
# command = b"pipeline PIPELINE0 regrst syn_counts_reg_0 rst_index 1\n"

# Function to connect to telnet server and send command
def telnet_session(host, port, command, timeout):
    
    try:
        # Connect to the telnet server
        tn = telnetlib.Telnet(host, port, timeout)
        
        # Read until prompt or login message
        tn.read_until(b"Escape character is", timeout)
        
        # Send command
        # tn.write(command)
        
        # Continue reading output (optional)
        while True:
            tn.write(command)
            output = tn.read_until(b"\n", timeout)
            # print(output.decode('utf-8'), end='')  # Print or process the output as needed
            print("SYN packet count reset ...")
            time.sleep(1)  # Adjust as needed to control frequency of command sending

    except Exception as e:
        print(f"Error: {e}")

    finally:
        tn.close()

# Start the telnet session
telnet_session(host, port, command, timeout)
