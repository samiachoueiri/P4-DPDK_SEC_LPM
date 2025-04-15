import csv
from collections import Counter

# Function to read the CSV, count occurrences, and write the result to another CSV
def count_ip_occurrences(input_file, output_file):
    # Initialize a list to store all IP addresses
    ip_addresses = []

    # Read the input CSV file
    with open(input_file, mode='r', newline='') as infile:
        csv_reader = csv.reader(infile)
        # Skip header if present
        next(csv_reader, None)
        
        # Read each IP address and append it to the list
        for row in csv_reader:
            if row:  # Ensure the row is not empty
                ip_addresses.append(row[0])
    
    # Count the occurrences of each IP address using Counter
    ip_counts = Counter(ip_addresses)

    # Sort the IPs in increasing order
    sorted_ips = sorted(ip_counts.items(), key=lambda x: x[0])

    # Write the results to the output CSV file
    with open(output_file, mode='w', newline='') as outfile:
        csv_writer = csv.writer(outfile)
        # Write header
        csv_writer.writerow(['src_ip', 'count'])
        
        # Write each IP and its count in sorted order
        for ip, count in sorted_ips:
            csv_writer.writerow([ip, count])

    print(f"IP counts have been written to {output_file}")

# Example usage:
input_file = 'src_ips.csv'  # Input CSV file with one column of IP addresses
output_file = 'src_ips_count.csv'  # Output CSV file with IPs and their count

count_ip_occurrences(input_file, output_file)
