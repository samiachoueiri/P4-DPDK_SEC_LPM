import telnetlib
import time

# Telnet server details
host = "0.0.0.0"
port = 8086
timeout = 1
sps = 5

attack0 = b"pipeline PIPELINE0 regrd attack index 0\n"
attack1 = b"pipeline PIPELINE1 regrd attack index 0\n"
attack2 = b"pipeline PIPELINE2 regrd attack index 0\n"
attack3 = b"pipeline PIPELINE3 regrd attack index 0\n"
attack4 = b"pipeline PIPELINE4 regrd attack index 0\n"
attack5 = b"pipeline PIPELINE5 regrd attack index 0\n"
attack6 = b"pipeline PIPELINE6 regrd attack index 0\n"
attack7 = b"pipeline PIPELINE7 regrd attack index 0\n"

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
hh_ts1_4 = b"pipeline PIPELINE4 regrd reg_timestamp1 index 0\n"
hh_ts1_5 = b"pipeline PIPELINE5 regrd reg_timestamp1 index 0\n"
hh_ts1_6 = b"pipeline PIPELINE6 regrd reg_timestamp1 index 0\n"
hh_ts1_7 = b"pipeline PIPELINE7 regrd reg_timestamp1 index 0\n"

hh_ts2_0 = b"pipeline PIPELINE0 regrd reg_timestamp2 index 0\n"
hh_ts2_1 = b"pipeline PIPELINE1 regrd reg_timestamp2 index 0\n"
hh_ts2_2 = b"pipeline PIPELINE2 regrd reg_timestamp2 index 0\n"
hh_ts2_3 = b"pipeline PIPELINE3 regrd reg_timestamp2 index 0\n"
hh_ts2_4 = b"pipeline PIPELINE4 regrd reg_timestamp2 index 0\n"
hh_ts2_5 = b"pipeline PIPELINE5 regrd reg_timestamp2 index 0\n"
hh_ts2_6 = b"pipeline PIPELINE6 regrd reg_timestamp2 index 0\n"
hh_ts2_7 = b"pipeline PIPELINE7 regrd reg_timestamp2 index 0\n"

hh_ts3_0 = b"pipeline PIPELINE0 regrd reg_timestamp3 index 0\n"
hh_ts3_1 = b"pipeline PIPELINE1 regrd reg_timestamp3 index 0\n"
hh_ts3_2 = b"pipeline PIPELINE2 regrd reg_timestamp3 index 0\n"
hh_ts3_3 = b"pipeline PIPELINE3 regrd reg_timestamp3 index 0\n"
hh_ts3_4 = b"pipeline PIPELINE4 regrd reg_timestamp3 index 0\n"
hh_ts3_5 = b"pipeline PIPELINE5 regrd reg_timestamp3 index 0\n"
hh_ts3_6 = b"pipeline PIPELINE6 regrd reg_timestamp3 index 0\n"
hh_ts3_7 = b"pipeline PIPELINE7 regrd reg_timestamp3 index 0\n"

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

                tn.write(attack4)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                attack4_hex = string_output.split(' ')[1].strip()

                tn.write(attack5)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                attack5_hex = string_output.split(' ')[1].strip()

                tn.write(attack6)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                attack6_hex = string_output.split(' ')[1].strip()

                tn.write(attack7)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                attack7_hex = string_output.split(' ')[1].strip()

                print("attack:","P0",attack0_hex,"P1",attack1_hex,"P2",attack2_hex,"P3",attack3_hex,"P4",attack4_hex,"P5",attack5_hex,"P6",attack6_hex,"P7",attack7_hex)

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

                tn.write(hh_ts1_4)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts14_hex = string_output.split(' ')[1].strip()
                ts14_dec = int(ts14_hex, 16)

                tn.write(hh_ts1_5)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts15_hex = string_output.split(' ')[1].strip()
                ts15_dec = int(ts15_hex, 16)

                tn.write(hh_ts1_6)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts16_hex = string_output.split(' ')[1].strip()
                ts16_dec = int(ts16_hex, 16)

                tn.write(hh_ts1_7)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts17_hex = string_output.split(' ')[1].strip()
                ts17_dec = int(ts17_hex, 16)

                print("HH_ts1:","ts1_0",ts10_dec,"ts1_1",ts11_dec,"ts1_2",ts12_dec,"ts1_3",ts13_dec,"ts1_4",ts14_dec,"ts1_5",ts15_dec,"ts1_6",ts16_dec,"ts1_7",ts17_dec)

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

                tn.write(hh_ts2_4)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts24_hex = string_output.split(' ')[1].strip()
                ts24_dec = int(ts24_hex, 16)

                tn.write(hh_ts2_5)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts25_hex = string_output.split(' ')[1].strip()
                ts25_dec = int(ts25_hex, 16)

                tn.write(hh_ts2_6)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts26_hex = string_output.split(' ')[1].strip()
                ts26_dec = int(ts26_hex, 16)

                tn.write(hh_ts2_7)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts27_hex = string_output.split(' ')[1].strip()
                ts27_dec = int(ts27_hex, 16)

                print("HH_ts2:","ts2_0",ts20_dec,"ts2_1",ts21_dec,"ts2_2",ts22_dec,"ts2_3",ts23_dec,"ts2_4",ts24_dec,"ts2_5",ts25_dec,"ts2_6",ts26_dec,"ts2_7",ts27_dec)

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

                tn.write(hh_ts3_4)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts34_hex = string_output.split(' ')[1].strip()
                ts34_dec = int(ts34_hex, 16)

                tn.write(hh_ts3_5)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts35_hex = string_output.split(' ')[1].strip()
                ts35_dec = int(ts35_hex, 16)

                tn.write(hh_ts3_6)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts36_hex = string_output.split(' ')[1].strip()
                ts36_dec = int(ts36_hex, 16)

                tn.write(hh_ts3_7)
                output = tn.read_until(b"\n", timeout)
                string_output = output.decode('utf-8')
                ts37_hex = string_output.split(' ')[1].strip()
                ts37_dec = int(ts37_hex, 16)

                print("HH_ts3:","ts3_0",ts30_dec,"ts3_1",ts31_dec,"ts3_2",ts32_dec,"ts3_3",ts33_dec,"ts3_4",ts34_dec,"ts3_5",ts35_dec,"ts3_6",ts36_dec,"ts3_7",ts37_dec)

                print("++++++++++++++++++++++++++++++++++++++++++++++++")
                inf0 = ts30_dec - ts20_dec
                inf1 = ts31_dec - ts21_dec
                inf2 = ts32_dec - ts22_dec
                inf3 = ts33_dec - ts23_dec
                inf4 = ts34_dec - ts24_dec
                inf5 = ts35_dec - ts25_dec
                inf6 = ts36_dec - ts26_dec
                inf7 = ts37_dec - ts27_dec
                print("inf:",inf0,inf1,inf2,inf3,inf4,inf5,inf6,inf7)
                print('sum:', inf0+inf1+inf2+inf3+inf4+inf5+inf6+inf7)
                print('avg:', (inf0+inf1+inf2+inf3+inf4+inf5+inf6+inf7)/8)
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
