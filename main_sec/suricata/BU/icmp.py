from scapy.all import Ether, IP, ICMP, send

# Define source and destination IP addresses
src_ip = "192.168.20.10"
dst_ip = "192.168.10.10"

# Define source and destination MAC addresses
src_mac = "00:00:00:00:00:03"  # Replace with actual source MAC address
dst_mac = "00:00:00:00:00:22"  # Replace with actual destination MAC address

# Define the ICMP Echo Request packets
for i in range(11):
    # Create the Ethernet layer with source and destination MAC addresses
    ether_layer = Ether(src=src_mac, dst=dst_mac)
    
    # Create the IP layer
    ip_packet = IP(src=src_ip, dst=dst_ip)
    
    # Create the ICMP Echo Request (Type 8) packet
    icmp_packet = ICMP(type=8, id=1000, seq=i+1)
    
    # Combine Ethernet, IP, and ICMP layers to create the complete packet
    packet = ether_layer/ip_packet/icmp_packet
    
    # Send the packet
    send(packet)
    print(f"Sent ICMP Echo Request packet {i+1} from {src_ip} to {dst_ip} with MAC addresses {src_mac} -> {dst_mac}")
