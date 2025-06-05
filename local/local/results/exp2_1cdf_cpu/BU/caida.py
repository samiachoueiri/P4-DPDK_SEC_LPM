import csv
import matplotlib.pyplot as plt

# Initialize lists to store data
packet_sizes = []
jan1_count = []
jan2_count = []

# Read data from CSV file
with open('caida.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        packet_sizes.append(int(row[0]))
        jan1_count.append(float(row[1]))
        jan2_count.append(float(row[2]))

# Plotting
plt.figure(figsize=(8, 5))
plt.rcParams.update({'font.size': 12}) #16

# Plotting percentage of packet count
plt.plot(packet_sizes, jan1_count, label='Dataset 3')
plt.plot(packet_sizes, jan2_count, label='Dataset 4')

# Adding labels and title
plt.xlabel('Packet Size (Bytes)')
plt.ylabel('Cummulative Percentage')
#plt.title('Packet Size Distribution')
plt.legend()

# Display plot
plt.grid(True)
plt.savefig("caida.pdf")
# plt.savefig("data.png")
plt.show()

