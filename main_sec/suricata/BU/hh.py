from scapy.all import IP, TCP, send

# Define source and destination IP addresses
src_ip = "192.168.20.10"
dst_ip = "192.168.10.10"

# Define the TCP packet details
for i in range(12):
    # Create the IP layer
    ip_packet = IP(src=src_ip, dst=dst_ip)
    
    # Create the TCP layer
    tcp_packet = TCP(sport=12345, dport=80, flags="", seq=1000+i)
    
    # Combine IP and TCP layers to create the complete packet
    packet = ip_packet/tcp_packet
    
    # Send the packet
    send(packet)
    print(f"Sent packet {i+1} from {src_ip} to {dst_ip}")
