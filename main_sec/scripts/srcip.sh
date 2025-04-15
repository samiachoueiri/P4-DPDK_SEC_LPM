#!/bin/bash

# Interface to capture packets on
INTERFACE="enp8s0np1"  # Change this to your desired network interface (e.g., enp7s0np0)
OUTPUT_FILE="src_ips.csv"

# Check if tcpdump is installed
if ! command -v tcpdump &> /dev/null; then
    echo "tcpdump is required but not installed. Please install it."
    exit 1
fi

# Initialize the CSV file with a header if it doesn't exist
if [ ! -f "$OUTPUT_FILE" ]; then
    echo "src_ip" > "$OUTPUT_FILE"
fi

# Capture packets on the specified interface and extract the source IPs
# Use tcpdump to sniff traffic and extract the source IP address from each packet
# Use awk to parse the output and extract just the source IP address
# Append each source IP to the CSV file continuously

echo "Capturing packets on interface $INTERFACE and writing source IPs to $OUTPUT_FILE..."

# Run tcpdump indefinitely and process each packet
sudo tcpdump -i "$INTERFACE" -nn -l | \
    awk '{print $3}' | \
    cut -d '.' -f 1-4 | \
    while read ip; do
        # Append the source IP to the CSV file continuously
        echo "$ip" >> "$OUTPUT_FILE"
    done
