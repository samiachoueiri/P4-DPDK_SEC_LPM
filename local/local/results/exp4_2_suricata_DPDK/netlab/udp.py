from scapy.all import IP, UDP, send
import ipaddress

# Define the initial IP address and the number of packets
initial_ip = "192.168.20.10"
dst_ip = "192.168.10.10"
num_packets = 100

# Convert the initial IP address to an ipaddress object
start_ip = ipaddress.IPv4Address(initial_ip)

# Send UDP packets
for i in range(num_packets):
    # Increment the IP address for each packet
    # src_ip = str(start_ip + i)
    src_ip = str(start_ip)
    
    # Create the IP layer
    ip_packet = IP(src=src_ip, dst=dst_ip)
    
    # Create the UDP packet (use arbitrary source and destination ports)
    udp_packet = UDP(sport=12345, dport=80)
    
    # Combine IP and UDP layers to create the complete packet
    packet = ip_packet/udp_packet
    
    # Send the packet
    send(packet)
    print(f"Sent UDP packet {i+1} from {src_ip} to {dst_ip}")
