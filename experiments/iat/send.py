#!/usr/bin/env python3
import argparse
import sys
import socket
import random
import struct
import netifaces as ni
import time
from scapy.all import sendp, send, get_if_list, get_if_hwaddr, PacketListField
from scapy.all import Packet, BitField, bind_layers, ShortField
from scapy.all import Ether, IP, UDP, TCP, sendpfast

def get_if():
    ifs=get_if_list()
    iface=None 
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print("Cannot find eth0 interface")
        exit(1)
    return iface

class my_custom_h(Packet):
    name="my_custom_header"
    fields_desc=[BitField("ingress_port", 0, 16),
            BitField("egress_port", 0, 16),
            BitField("packet_length",0,32)]

class queue_statistics(Packet):
   name="queue_statistics"
   fields_desc=[BitField("switch_ID", 0, 8),
                BitField("enq_timestamp", 0, 32),
                BitField("deq_timestamp", 0, 48),
                BitField("q_delay", 0, 48),
                BitField("q_length",0,24)]
   def extract_padding(self,p):
       return "",p
 
class layers(Packet):
    name="layer_count"
    fields_desc=[ShortField("count", 0),
    PacketListField("traces", [], queue_statistics,
                    count_from=lambda pkt:(pkt.count*1))]
    
class interarrival(Packet):
    name="interarrival"
    fields_desc=[BitField("interarrival_time", 0, 48)]
    def extract_padding(self,p):
        return "",p

def main():

    if len(sys.argv) < 3:
        print('Pass at least 2 arguments: <destination> "<message>" "<key>" "<custom_protocol>"')
        exit(1)
    
    iface = ni.interfaces()[1] 
    host_ip = ni.ifaddresses(iface)[ni.AF_INET][0]['addr']
    dst_addr = socket.gethostbyname(sys.argv[1])
    host_mac_addr =  ni.ifaddresses(iface)[ni.AF_LINK][0]['addr']
    #ARP table
    if dst_addr == "192.168.10.1":
        dst_mac_addr = "00:00:00:00:00:01"
    elif dst_addr == "192.168.10.2":
        dst_mac_addr = "00:00:00:00:00:02"
    elif dst_addr == "192.168.10.3":
        dst_mac_addr = "00:00:00:00:00:03"
    elif dst_addr == "192.168.10.4":
        dst_mac_addr = "00:00:00:00:00:04"
    pps = 10
    #Compose the Ethernet header
    pkt = Ether(src=host_mac_addr, dst=dst_mac_addr)
    probe_flag = 0
    if len(sys.argv) > 3:
        key = sys.argv[3]
        protocol = sys.argv[4]
        if key == "-p":
            if protocol == "custom":
                bind_layers(IP, my_custom_h)
                pkt = pkt / IP(src=host_ip, dst=dst_addr) / my_custom_h() / sys.argv[2]
            elif protocol == "probe":
                bind_layers(IP, queue_statistics)
                pkt = pkt / IP(src=host_ip, dst=dst_addr,proto=int('FD',16)) / queue_statistics() / sys.argv[2]
                probe_flag = 1
            elif protocol == "stack":
                bind_layers(UDP, layers)
                probe_flag = 1
                pkt = pkt / IP(src=host_ip, dst=dst_addr, proto=17) / UDP(sport=4321,dport=2001) / layers() / sys.argv[2]
            elif protocol == "interarrival":
                pkt = pkt / IP(src=host_ip, dst=dst_addr, proto=int('FF',16)) / interarrival()
                pps = int(sys.argv[2])
                probe_flag=2
                print("Sending packet at",pps,"packets per second")
            else:
                print("Wrong protocol, use 'custom'")
                exit(1)
        else:
            print("Wrong key, use '-p'")
            exit(1)
    else:
       pkt = pkt / IP(src=host_ip,dst=dst_addr) / sys.argv[2]
    
    if probe_flag == 1:
        while 1: 
            print(("sending on interface %s to %s" % (iface, str(dst_addr))))
            sendp(pkt, iface=iface, verbose=False)
            pkt.show2()
            time.sleep(0.01)
    elif probe_flag == 2:
            sendpfast(pkt,pps=pps, loop=10000)
    else:
            print(("sending on interface %s to %s" % (iface, str(dst_addr))))
            sendp(pkt, iface=iface, verbose=False)
            pkt.show2()
 
if __name__ == '__main__':
    main()
