# !/bin/bash

# Path to the CSV file
output_csv="network_packets.csv"

# Write CSV header (only needed once at the start)
echo "timestamp,rx_packets,tx_packets" > "$output_csv"

# Continuous monitoring loop
while true; do
# for ((i = 0; i < 1000; i++)); do
    # Run the command and extract the received and transmitted packets on the physical layer
    tx=$(ethtool -S enp7s0np0 | grep -E 'tx_packets_phy' | awk '{print $2}')
    rx=$(ethtool -S enp7s0np0 | grep -E 'rx_packets_phy' | awk '{print $2}')

    # Get the current timestamp
    timestamp=$(date +"%T.%6N")

    # Append data to the CSV file
    echo "$timestamp,$rx,$tx" >> "$output_csv"

    # Sleep for 0.1 seconds before running the command again
    sleep 0.1
done
