import telnetlib
import time

# Telnet server details
host = "0.0.0.0"
port = 8086
timeout = 1
sps = 5

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

flow0 = b"pipeline PIPELINE1 regrd get_tcp_flow_flow_id0 index 0\n"
flow1 = b"pipeline PIPELINE1 regrd get_tcp_flow_flow_id1 index 0\n"
flow2 = b"pipeline PIPELINE1 regrd get_tcp_flow_flow_id2 index 0\n"
flow3 = b"pipeline PIPELINE1 regrd get_tcp_flow_flow_id3 index 0\n"

ht0_tcp = b"pipeline PIPELINE1 regrd heavy_hitter_ht0 index 0x330C\n"
ht1_tcp = b"pipeline PIPELINE1 regrd heavy_hitter_ht1 index 0x3370\n"
ht2_tcp = b"pipeline PIPELINE1 regrd heavy_hitter_ht2 index 0x33D4\n"
ht3_tcp = b"pipeline PIPELINE1 regrd heavy_hitter_ht3 index 0x3438\n"

hh_ts1_0 = b"pipeline PIPELINE0 regrd reg_timestamp1 index 0\n"
hh_ts1_1 = b"pipeline PIPELINE1 regrd reg_timestamp1 index 0\n"
hh_ts1_2 = b"pipeline PIPELINE2 regrd reg_timestamp1 index 0\n"
hh_ts1_3 = b"pipeline PIPELINE3 regrd reg_timestamp1 index 0\n"

hh_ts2_0 = b"pipeline PIPELINE0 regrd reg_timestamp2 index 0\n"
hh_ts2_1 = b"pipeline PIPELINE1 regrd reg_timestamp2 index 0\n"
hh_ts2_2 = b"pipeline PIPELINE2 regrd reg_timestamp2 index 0\n"
hh_ts2_3 = b"pipeline PIPELINE3 regrd reg_timestamp2 index 0\n"

hh_ts3_0 = b"pipeline PIPELINE0 regrd reg_timestamp3 index 0\n"
hh_ts3_1 = b"pipeline PIPELINE1 regrd reg_timestamp3 index 0\n"
hh_ts3_2 = b"pipeline PIPELINE2 regrd reg_timestamp3 index 0\n"
hh_ts3_3 = b"pipeline PIPELINE3 regrd reg_timestamp3 index 0\n"

# icmp0 = b"pipeline PIPELINE0 regrd get_icmp_flow_flow_icmp_id0 index 0\n"
# icmp1 = b"pipeline PIPELINE0 regrd get_icmp_flow_flow_icmp_id1 index 0\n"
# icmp2 = b"pipeline PIPELINE0 regrd get_icmp_flow_flow_icmp_id2 index 0\n"
# icmp3 = b"pipeline PIPELINE0 regrd get_icmp_flow_flow_icmp_id3 index 0\n"

# ht0_icmp = b"pipeline PIPELINE0 regrd icmp_flood_ht_icmp index 0x7e11\n"
# ht1_icmp = b"pipeline PIPELINE0 regrd icmp_flood_ht_icmp_0 index 0x7e75\n"
# ht2_icmp = b"pipeline PIPELINE0 regrd icmp_flood_ht_icmp_1 index 0x7ed9\n"
# ht3_icmp = b"pipeline PIPELINE0 regrd icmp_flood_ht_icmp_2 index 0x7f3d\n"

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

                tn.write(flow0)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow0_hex = string_output.split(' ')[1].strip()
                flow0_dec = int(flow0_hex, 16)

                tn.write(flow1)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow1_hex = string_output.split(' ')[1].strip()
                flow1_dec = int(flow1_hex, 16)

                tn.write(flow2)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow2_hex = string_output.split(' ')[1].strip()
                flow2_dec = int(flow2_hex, 16)

                tn.write(flow3)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                flow3_hex = string_output.split(' ')[1].strip()
                flow3_dec = int(flow3_hex, 16)

                print("TCP flow:","h0",flow0_hex,"h1",flow1_hex,"h2",flow2_hex,"h3",flow3_hex)

                tn.write(ht0_tcp)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ht0_hex = string_output.split(' ')[1].strip()
                ht0_dec = int(ht0_hex, 16)

                tn.write(ht1_tcp)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ht1_hex = string_output.split(' ')[1].strip()
                ht1_dec = int(ht1_hex, 16)

                tn.write(ht2_tcp)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ht2_hex = string_output.split(' ')[1].strip()
                ht2_dec = int(ht2_hex, 16)

                tn.write(ht3_tcp)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ht3_hex = string_output.split(' ')[1].strip()
                ht3_dec = int(ht3_hex, 16)

                print("TCP count:","h0",ht0_dec,"h1",ht1_dec,"h2",ht2_dec,"h3",ht3_dec)

                tn.write(hh_ts1_0)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts10_hex = string_output.split(' ')[1].strip()
                ts10_dec = int(ts10_hex, 16)

                tn.write(hh_ts1_1)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts11_hex = string_output.split(' ')[1].strip()
                ts11_dec = int(ts11_hex, 16)

                tn.write(hh_ts1_2)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts12_hex = string_output.split(' ')[1].strip()
                ts12_dec = int(ts12_hex, 16)

                tn.write(hh_ts1_3)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts13_hex = string_output.split(' ')[1].strip()
                ts13_dec = int(ts13_hex, 16)

                print("HH_ts1:","ts1_0",ts10_dec,"ts1_1",ts11_dec,"ts1_2",ts12_dec,"ts1_3",ts13_dec)

                tn.write(hh_ts2_0)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts20_hex = string_output.split(' ')[1].strip()
                ts20_dec = int(ts20_hex, 16)

                tn.write(hh_ts2_1)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts21_hex = string_output.split(' ')[1].strip()
                ts21_dec = int(ts21_hex, 16)

                tn.write(hh_ts2_2)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts22_hex = string_output.split(' ')[1].strip()
                ts22_dec = int(ts22_hex, 16)

                tn.write(hh_ts2_3)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts23_hex = string_output.split(' ')[1].strip()
                ts23_dec = int(ts23_hex, 16)

                print("HH_ts2:","ts2_0",ts20_dec,"ts2_1",ts21_dec,"ts2_2",ts22_dec,"ts2_3",ts23_dec)

                tn.write(hh_ts3_0)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts30_hex = string_output.split(' ')[1].strip()
                ts30_dec = int(ts30_hex, 16)

                tn.write(hh_ts3_1)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts31_hex = string_output.split(' ')[1].strip()
                ts31_dec = int(ts31_hex, 16)

                tn.write(hh_ts3_2)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts32_hex = string_output.split(' ')[1].strip()
                ts32_dec = int(ts32_hex, 16)

                tn.write(hh_ts3_3)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts33_hex = string_output.split(' ')[1].strip()
                ts33_dec = int(ts33_hex, 16)

                print("HH_ts3:","ts3_0",ts30_dec,"ts3_1",ts31_dec,"ts3_2",ts32_dec,"ts3_3",ts33_dec)

                # print("------ ICMP")

                # tn.write(icmp0)
                # output = tn.read_until(b"\n", timeout)
                # string_output = output.decode('utf-8')
                # icmp0_hex = string_output.split(' ')[1].strip()
                # icmp0_dec = int(icmp0_hex, 16)

                # tn.write(icmp1)
                # output = tn.read_until(b"\n", timeout)
                # string_output = output.decode('utf-8')
                # icmp1_hex = string_output.split(' ')[1].strip()
                # icmp1_dec = int(icmp1_hex, 16)

                # tn.write(icmp2)
                # output = tn.read_until(b"\n", timeout)
                # string_output = output.decode('utf-8')
                # icmp2_hex = string_output.split(' ')[1].strip()
                # icmp2_dec = int(icmp2_hex, 16)

                # tn.write(icmp3)
                # output = tn.read_until(b"\n", timeout)
                # string_output = output.decode('utf-8')
                # icmp3_hex = string_output.split(' ')[1].strip()
                # icmp3_dec = int(icmp3_hex, 16)

                # print("ICMP flow:","h0",icmp0_hex,"h1",icmp1_hex,"h2",icmp2_hex,"h3",icmp3_hex)

                # tn.write(ht0_icmp)
                # output = tn.read_until(b"\n", timeout)
                # string_output = output.decode('utf-8')
                # ht0_hex = string_output.split(' ')[1].strip()
                # ht0_dec = int(ht0_hex, 16)

                # tn.write(ht1_icmp)
                # output = tn.read_until(b"\n", timeout)
                # string_output = output.decode('utf-8')
                # ht1_hex = string_output.split(' ')[1].strip()
                # ht1_dec = int(ht1_hex, 16)

                # tn.write(ht2_icmp)
                # output = tn.read_until(b"\n", timeout)
                # string_output = output.decode('utf-8')
                # ht2_hex = string_output.split(' ')[1].strip()
                # ht2_dec = int(ht2_hex, 16)

                # tn.write(ht3_icmp)
                # output = tn.read_until(b"\n", timeout)
                # string_output = output.decode('utf-8')
                # ht3_hex = string_output.split(' ')[1].strip()
                # ht3_dec = int(ht3_hex, 16)

                # print("ICMP count:","h0",ht0_dec,"h1",ht1_dec,"h2",ht2_dec,"h3",ht3_dec)

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
