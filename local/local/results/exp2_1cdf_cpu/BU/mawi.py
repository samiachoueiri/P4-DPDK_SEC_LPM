import csv
import matplotlib.pyplot as plt

# Initialize lists to store data
packet_sizes = []
mar_count = []
oct_count = []

# Read data from CSV file
with open('mawi.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        packet_sizes.append(int(row[0]))
        mar_count.append(float(row[1]))
        oct_count.append(float(row[2]))

# Plotting
plt.figure(figsize=(8, 5))
plt.rcParams.update({'font.size': 12}) #16

# Plotting percentage of packet count
plt.plot(packet_sizes, mar_count, label='Dataset 1')
plt.plot(packet_sizes, oct_count, label='Dataset 2')

# Adding labels and title
plt.xlabel('Packet Size (Bytes)')
plt.ylabel('Cummulative Percentage')
#plt.title('Packet Size Distribution')
plt.legend()

# Display plot
plt.grid(True)
plt.savefig("mawi.pdf")
# plt.savefig("data.png")
plt.show()

