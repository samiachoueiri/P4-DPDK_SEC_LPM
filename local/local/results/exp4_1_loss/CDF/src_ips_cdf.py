import csv
import matplotlib.pyplot as plt

# Initialize lists to store data
src_ip = []
count = []

# Read data from CSV file
with open('src_ips_cdf.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        src_ip.append(row[0])
        count.append(float(row[1]))

# Plotting
plt.figure(figsize=(8, 5))
plt.rcParams.update({'font.size': 12}) #16

# Plotting percentage of packet count
plt.plot(src_ip, count, label='Dataset 3')

# Adding labels and title
plt.xlabel('Flow Source IP Address')
plt.ylabel('Cummulative Percentage (%)')
#plt.title('Packet Size Distribution')

# Adjust the x-axis to show only a couple of IP addresses
# Select the indices where you want to show the ticks
num_ticks = 15  # You can adjust this number
tick_indices = range(0, len(src_ip), max(1, len(src_ip) // num_ticks))  # Select evenly spaced ticks
tick_labels = [src_ip[i] for i in tick_indices]  # Corresponding IP addresses for the ticks

# Set the x-axis ticks to show only a few IPs
plt.xticks(tick_indices, tick_labels, rotation=45)  # Rotate the labels for better visibility



# plt.legend()

# Display plot
plt.grid(True)
plt.savefig("src_ips_cdf.pdf")
# plt.savefig("data.png")
plt.show()

