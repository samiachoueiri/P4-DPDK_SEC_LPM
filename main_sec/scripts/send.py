from scapy.all import *
import time

srcMAC = "00:00:00:00:00:03"
dstMAC = "00:00:00:00:00:22"
srcIP = "192.168.20.1"
dstIP = "192.168.10.1"
# ########################################## attack 1 sending a TCP SYN packet from h3 to h1
# eth = Ether(src= srcMAC, dst= dstMAC, type=0x0800)  
# ip = IP(src= srcIP , dst= dstIP, proto=0x06)
# tcp = TCP(sport=1234, dport=80, flags="S")
# pkt = eth/ip/tcp

########################################## attack 5 sending a TCP packet from h3 to h1
eth = Ether(src= srcMAC, dst= dstMAC, type=0x0800)  
ip = IP(src= srcIP , dst= dstIP, proto=0x06)
tcp = TCP(sport=1234, dport=80, flags="")
pkt = eth/ip/tcp

# ########################################## attack 7 sending a UDP packet from h3 to h1
# eth = Ether(src= srcMAC, dst= dstMAC, type=0x0800)
# ip = IP(src= srcIP, dst= dstIP, proto=0x11)
# udp = UDP(sport=1234, dport=80)
# pkt = eth/ip/udp


# sendp(pkt, iface="enp7s0np0")

while True:
    sendp(pkt, iface="enp7s0np0")
    time.sleep(1)