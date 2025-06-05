import csv
import matplotlib.pyplot as plt

# Initialize lists to store data
packet_sizes_mawi = []
mar_count = []
oct_count = []

# Read data from CSV file
with open('mawi.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        packet_sizes_mawi.append(int(row[0]))
        mar_count.append(float(row[1]))
        oct_count.append(float(row[2]))

# Initialize lists to store data
packet_sizes_caida = []
jan1_count = []
jan2_count = []

# Read data from CSV file
with open('caida.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        packet_sizes_caida.append(int(row[0]))
        jan1_count.append(float(row[1]))
        jan2_count.append(float(row[2]))

# Plotting
plt.figure(figsize=(8, 5))
plt.rcParams.update({'font.size': 12}) #16

# Plotting percentage of packet count
plt.plot(packet_sizes_mawi, mar_count, label='Dataset 1')
plt.plot(packet_sizes_mawi, oct_count, label='Dataset 2')
plt.plot(packet_sizes_caida, jan1_count, label='Dataset 3')
plt.plot(packet_sizes_caida, jan2_count, label='Dataset 4')

plt.xlim(0,1501)
plt.xticks([64,128,256,512,1024,1500])
# plt.xticklabels(['1', '1.5', '3', '5','10'], fontsize=fsize - 1)  # Custom labels for the right y-axis

# Adding labels and title
plt.xlabel('Packet Size (Bytes)')
plt.ylabel('Cummulative Percentage')
#plt.title('Packet Size Distribution')
plt.legend()

# Display plot
plt.grid(True)
plt.savefig("mawi_caida.pdf")
# plt.savefig("data.png")
plt.show()

