import telnetlib
import time

# Telnet server details
host = "0.0.0.0"
port = 8086
timeout = 1

# Function to connect to telnet server and send command
def telnet_session(host, port, timeout):
    
    try:
        # Connect to the telnet server
        tn = telnetlib.Telnet(host, port, timeout)
        
        # Read until prompt or login message
        tn.read_until(b"Escape character is", timeout)

        while True:
            tn.write(b"pipeline PIPELINE0 regwr syn_flood_syn_counts_reg value 0 index 0\n")
            print("SYN packet count reset ...")
            time.sleep(1)  # Adjust as needed to control frequency of command sending

    except Exception as e:
        print(f"Error: {e}")

    finally:
        tn.close()

# Start the telnet session
telnet_session(host, port, timeout)