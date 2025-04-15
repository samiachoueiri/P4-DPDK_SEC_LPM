from scapy.all import Ether, IP, TCP, send
import ipaddress

# Define the initial IP address and the number of packets
initial_ip = "192.168.20.10"
dst_ip = "192.168.10.1"

# Define source and destination MAC addresses
src_mac = "00:00:00:00:00:03"  # Replace with actual source MAC address
dst_mac = "00:00:00:00:00:22"  # Replace with actual destination MAC address

num_packets = 1

# Convert the initial IP address to an ipaddress object
start_ip = ipaddress.IPv4Address(initial_ip)

# Send TCP SYN-ACK packets
for i in range(num_packets):
    # Increment the IP address for each packet
    src_ip = str(start_ip)
    ether_layer = Ether(src=src_mac, dst=dst_mac)
    # Create the IP layer
    ip_packet = IP(src=src_ip, dst=dst_ip)
    
    # Create the TCP SYN-ACK packet (flags="SA" for SYN and ACK)
    tcp_packet = TCP(sport=12345, dport=80, flags="SA", seq=1000+i, ack=1)
    
    # Combine IP and TCP layers to create the complete packet
    packet = ether_layer/ip_packet/tcp_packet
    
    # Send the packet
    send(packet)
    print(f"Sent TCP SYN-ACK packet {i+1} from {src_ip} to {dst_ip}")
