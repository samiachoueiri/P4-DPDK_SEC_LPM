from scapy.all import IP, TCP, send
import ipaddress

# Define the initial IP address and the number of packets
initial_ip = "192.168.20.10"
dst_ip = "192.168.10.10"
num_packets = 5

# Convert the initial IP address to an ipaddress object
start_ip = ipaddress.IPv4Address(initial_ip)

# Send TCP FIN packets
for i in range(num_packets):
    # Increment the IP address for each packet
    src_ip = str(start_ip + i)
    
    # Create the IP layer
    ip_packet = IP(src=src_ip, dst=dst_ip)
    
    tcp_packet = TCP(sport=12345, dport=80, flags="R", seq=1000+i)
    # if (i%2==0):
    #     # Create the TCP FIN packet (flags='F' for FIN)
    #     tcp_packet = TCP(sport=12345, dport=80, flags="F", seq=1000+i)
    # else:
    #     tcp_packet = TCP(sport=12345, dport=80, flags="R", seq=1000+i)
    
    # Combine IP and TCP layers to create the complete packet
    packet = ip_packet/tcp_packet
    
    # Send the packet
    send(packet)
    print(f"Sent TCP FIN packet {i+1} from {src_ip} to {dst_ip}")
