import telnetlib
import time

# Telnet server details
host = "0.0.0.0"
port = 8086
timeout = 1
sps = 1

# Command to send
# get_index = b"pipeline PIPELINE0 regrd reg_index_0 index 0\n"
attack0 = b"pipeline PIPELINE0 regrd attack index 0\n"
attack1 = b"pipeline PIPELINE1 regrd attack index 0\n"
attack2 = b"pipeline PIPELINE2 regrd attack index 0\n"
attack3 = b"pipeline PIPELINE3 regrd attack index 0\n"

proto0 = b"pipeline PIPELINE0 regrd proto_0 index 0\n"
proto1 = b"pipeline PIPELINE1 regrd proto_0 index 0\n"
proto2 = b"pipeline PIPELINE2 regrd proto_0 index 0\n"
proto3 = b"pipeline PIPELINE3 regrd proto_0 index 0\n"

flow0_P0 = b"pipeline PIPELINE0 regrd get_tcp_flow_flow_id0 index 0\n"
flow1_P0 = b"pipeline PIPELINE0 regrd get_tcp_flow_flow_id1 index 0\n"
flow2_P0 = b"pipeline PIPELINE0 regrd get_tcp_flow_flow_id2 index 0\n"
flow3_P0 = b"pipeline PIPELINE0 regrd get_tcp_flow_flow_id3 index 0\n"

flow0_P1 = b"pipeline PIPELINE1 regrd get_tcp_flow_flow_id0 index 0\n"
flow1_P1 = b"pipeline PIPELINE1 regrd get_tcp_flow_flow_id1 index 0\n"
flow2_P1 = b"pipeline PIPELINE1 regrd get_tcp_flow_flow_id2 index 0\n"
flow3_P1 = b"pipeline PIPELINE1 regrd get_tcp_flow_flow_id3 index 0\n"

flow0_P2 = b"pipeline PIPELINE2 regrd get_tcp_flow_flow_id0 index 0\n"
flow1_P2 = b"pipeline PIPELINE2 regrd get_tcp_flow_flow_id1 index 0\n"
flow2_P2 = b"pipeline PIPELINE2 regrd get_tcp_flow_flow_id2 index 0\n"
flow3_P2 = b"pipeline PIPELINE2 regrd get_tcp_flow_flow_id3 index 0\n"

flow0_P3 = b"pipeline PIPELINE3 regrd get_tcp_flow_flow_id0 index 0\n"
flow1_P3 = b"pipeline PIPELINE3 regrd get_tcp_flow_flow_id1 index 0\n"
flow2_P3 = b"pipeline PIPELINE3 regrd get_tcp_flow_flow_id2 index 0\n"
flow3_P3 = b"pipeline PIPELINE3 regrd get_tcp_flow_flow_id3 index 0\n"

# Function to connect to telnet server and send command
def telnet_session(host, port, timeout):
    try:
        # Connect to the telnet server
        tn = telnetlib.Telnet(host, port, timeout)
        tn.read_until(b"Escape character is", timeout)

        # tn.write(get_index)
        # output = tn.read_until(b"\n", timeout)

        tn.write(attack0)
        output = tn.read_until(b"\n", timeout)
        
        while True:
            try:
                # tn.write(get_index)
                # output = tn.read_until(b"\n", timeout)
                # string_output = output.decode('utf-8')
                # index_hex = string_output.split(' ')[1].strip()
                # index_dec = int(index_hex, 16)
                # index_hex = '0x4270'

                # get_count = f"pipeline PIPELINE0 regrd ht0_0 index {index_hex}\n"
                # get_count = get_count.encode('utf-8')
                # tn.write(get_count)
                # output = tn.read_until(b"\n", timeout)
                # string_output = output.decode('utf-8')
                # count_hex = string_output.split(' ')[1]
                # count_dec = int(count_hex, 16)
                print("------ main")
                tn.write(attack0)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                attack0_hex = string_output.split(' ')[1].strip()

                tn.write(attack1)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                attack1_hex = string_output.split(' ')[1].strip()

                tn.write(attack2)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                attack2_hex = string_output.split(' ')[1].strip()

                tn.write(attack3)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                attack3_hex = string_output.split(' ')[1].strip()
                
                print("attack:","P0",attack0_hex,"P1",attack1_hex,"P2",attack2_hex,"P3",attack3_hex)

                tn.write(proto0)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                proto0_hex = string_output.split(' ')[1].strip()

                tn.write(proto1)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                proto1_hex = string_output.split(' ')[1].strip()

                tn.write(proto2)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                proto2_hex = string_output.split(' ')[1].strip()

                tn.write(proto3)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                proto3_hex = string_output.split(' ')[1].strip()
                
                print("proto:","P0",proto0_hex,"P1",proto1_hex,"P2",proto2_hex,"P3",proto3_hex)

                print("------ TCP")

                tn.write(flow0_P0)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow0_P0_hex = string_output.split(' ')[1].strip()
                flow0_P0_dec = int(flow0_P0_hex, 16)

                tn.write(flow1_P0)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow1_P0_hex = string_output.split(' ')[1].strip()
                flow1_P0_dec = int(flow1_P0_hex, 16)

                tn.write(flow2_P0)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow2_P0_hex = string_output.split(' ')[1].strip()
                flow2_P0_dec = int(flow2_P0_hex, 16)

                tn.write(flow3_P0)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow3_P0_hex = string_output.split(' ')[1].strip()
                flow3_P0_dec = int(flow3_P0_hex, 16)
                # flow3_P0_hex = 0
                print("TCP flow P0:","h0",flow0_P0_hex,"h1",flow1_P0_hex,"h2",flow2_P0_hex,"h3",flow3_P0_hex)

                tn.write(flow0_P1)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow0_P1_hex = string_output.split(' ')[1].strip()
                flow0_P1_dec = int(flow0_P1_hex, 16)

                tn.write(flow1_P1)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow1_P1_hex = string_output.split(' ')[1].strip()
                flow1_P1_dec = int(flow1_P1_hex, 16)

                tn.write(flow2_P1)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow2_P1_hex = string_output.split(' ')[1].strip()
                flow2_P1_dec = int(flow2_P1_hex, 16)

                tn.write(flow3_P1)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow3_P1_hex = string_output.split(' ')[1].strip()
                flow3_P1_dec = int(flow3_P1_hex, 16)
                # flow3_P1_hex = 0
                print("TCP flow P1:","h0",flow0_P1_hex,"h1",flow1_P1_hex,"h2",flow2_P1_hex,"h3",flow3_P1_hex)

                tn.write(flow0_P2)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow0_P2_hex = string_output.split(' ')[1].strip()
                flow0_P2_dec = int(flow0_P2_hex, 16)

                tn.write(flow1_P2)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow1_P2_hex = string_output.split(' ')[1].strip()
                flow1_P2_dec = int(flow1_P2_hex, 16)

                tn.write(flow2_P2)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow2_P2_hex = string_output.split(' ')[1].strip()
                flow2_P2_dec = int(flow2_P2_hex, 16)

                tn.write(flow3_P2)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow3_P2_hex = string_output.split(' ')[1].strip()
                flow3_P2_dec = int(flow3_P2_hex, 16)
                # flow3_P2_hex = 0
                print("TCP flow P2:","h0",flow0_P2_hex,"h1",flow1_P2_hex,"h2",flow2_P2_hex,"h3",flow3_P2_hex)

                tn.write(flow0_P3)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow0_P3_hex = string_output.split(' ')[1].strip()
                flow0_P3_dec = int(flow0_P3_hex, 16)

                tn.write(flow1_P3)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow1_P3_hex = string_output.split(' ')[1].strip()
                flow1_P3_dec = int(flow1_P3_hex, 16)

                tn.write(flow2_P3)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow2_P3_hex = string_output.split(' ')[1].strip()
                flow2_P3_dec = int(flow2_P3_hex, 16)

                tn.write(flow3_P3)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow3_P3_hex = string_output.split(' ')[1].strip()
                flow3_P3_dec = int(flow3_P3_hex, 16)
                # flow3_P3_hex = 0
                print("TCP flow P3:","h0",flow0_P3_hex,"h1",flow1_P3_hex,"h2",flow2_P3_hex,"h3",flow3_P3_hex)

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
