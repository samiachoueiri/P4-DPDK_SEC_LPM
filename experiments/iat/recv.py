#!/usr/bin/env python3
import sys
import struct
import os
import netifaces as ni

from scapy.all import sniff, sendp, hexdump, get_if_list, get_if_hwaddr,PacketListField
from scapy.all import Packet, IPOption, bind_layers
from scapy.all import ShortField, IntField, LongField, BitField, FieldListField, FieldLenField
from scapy.all import IP, TCP, UDP, Raw, ARP, Ether, IPv6
from scapy.layers.inet import _IPOption_HDR


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

def get_network_interfaces():
    interfaces = ni.interfaces()
    return interfaces

#my_custom_header definition

class my_custom_h(Packet):
    name="my_custom_header"
    fields_desc=[BitField("ingress_port", 0, 16),
                 BitField("egress_port", 0, 16),
                 BitField("packet_length",0,32)]

class queue_statistics(Packet):
    name="queue_statistics"
    fields_desc=[ BitField("switch_ID", 0, 8),
                 BitField("enq_timestamp", 0, 32),
                 BitField("deq_timestamp", 0, 48),
                 BitField("q_delay", 0, 48),
                 BitField("q_length",0,24)]
    def extract_padding(self, p):
        return "", p

class layers(Packet):
    name="layer_count"
    fields_desc=[ShortField("count",0),
    PacketListField("traces", [], queue_statistics,
                    count_from=lambda pkt:(pkt.count*1))]

class interarrival(Packet):
    name="interarrival"
    fields_desc=[BitField("interarrival_time", 0, 48)]
    def extract_padding(self, p):
        return "",p

def handle_pkt(pkt):
     global protocol
     if protocol == 'stack':
         if UDP in pkt and pkt[UDP].dport == int('2001'):
            pkt.show2()
     elif TCP in pkt:
         pkt.show2()
     elif not TCP in pkt:#Filtering iperf3 (TCP) packets 
         if not IPv6 in pkt:
             print("got a packet")
             pkt.show2()
             sys.stdout.flush()

'''
            stats = [str(pkt[queue_statistics].ingress_timestamp),"\n", 
                     str(pkt[queue_statistics].egress_timestamp),"\n",
                     str(pkt[queue_statistics].time_diff),"\n",
                     str(pkt[queue_statistics].q_length)]
            global_time = pkt[queue_statistics].ingress_timestamp/1000000
            file = open("i_tmstmp.dat","a")
            file.writelines(str(pkt[queue_statistics].ingress_timestamp))
            file.writelines("\n")
            file.close()
            file = open("e_tmstmp.dat","a")
            file.writelines(str(pkt[queue_statistics].egress_timestamp))
            file.writelines("\n")
            file.close()
            file = open("time_diff.dat","a")
            file.writelines(str(global_time))
            file.writelines(" ")
            file.writelines(str(pkt[queue_statistics].time_diff/1000))
            file.writelines("\n")
            file.close()
            file = open("q_length.dat","a")
            file.writelines(str(global_time))
            file.writelines(" ")
            file.writelines(str(pkt[queue_statistics].q_length))
            file.writelines("\n")
            file.close()
'''
protocol = "na"
def main():
    global protocol

    # ifaces = [i for i in os.listdir('/sys/class/net/') if 'eth' in i]
    ifaces = get_network_interfaces()
    iface = ifaces[1]
    
    if len(sys.argv) > 1:
        key = sys.argv[1]
        protocol = sys.argv[2]
        if key == "-p":
            if protocol == "custom":
                bind_layers(IP,my_custom_h)
            elif protocol == "probe":
                bind_layers(IP,queue_statistics)
            elif protocol == "stack":
                print("Receiving a packet with a header stack")
                bind_layers(UDP, layers)
            elif protocol == "interarrival":
                bind_layers(IP,interarrival)    
            else:
                print("Wrong protocol, use 'custom', 'probe', 'stack'")
                exit(1)
        else:
            print("Wrong key, use '-p' ")
            exit(1)
    
    print(("sniffing on %s" % iface))
   
    sys.stdout.flush()
    sniff(iface = iface, prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
