
# hping3 --flood -A -a 192.168.20.10 -p 80 192.168.10.10
# hping3 --flood -SA -a 192.168.20.10 -p 80 192.168.10.10

from scapy.all import IP, TCP, send
import ipaddress

# Define the initial IP address and the number of packets
initial_ip = "192.168.10.10"
dst_ip = "192.168.20.10"
num_packets = 5

# Convert the initial IP address to an ipaddress object
start_ip = ipaddress.IPv4Address(initial_ip)

# Send TCP SYN packets
for i in range(num_packets):
    # Increment the IP address for each packet
    # src_ip = str(start_ip +i)
    src_ip = str(start_ip)
    
    # Create the IP layer
    ip_packet = IP(src=src_ip, dst=dst_ip)
    
    # Create the TCP SYN packet (flags="S" for SYN)
    tcp_packet = TCP(sport=12345, dport=80, flags="A", seq=1000+i, ack=1)

    # Combine IP and TCP layers to create the complete packet
    packet = ip_packet/tcp_packet
    
    # Send the packet
    send(packet)
    print(f"Sent TCP SYN packet {i+1} from {src_ip} to {dst_ip}")
