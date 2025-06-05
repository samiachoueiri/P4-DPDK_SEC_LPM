import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap, Normalize

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
plt.figure(figsize=(14, 18))
plt.rcParams.update({'font.size': 16}) #16
plt.subplot(2, 1, 1)
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
plt.grid(True)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc="lower center", ncol=4, mode="expand", borderaxespad=0.,fontsize=16)

# ---------------------------------------------------------------------------------------------------------------------------
# Number of cores and packet sizes
cores = [1, 2, 3, 4, 5, 6, 7, 8]
packet_sizes = [64, 128, 256, 512, 1024, 1500]
throughput_data = [
    [1,3,6,12,25,36],  # Throughput for 1 core
    [3,6,13,25,50,73],  # Throughput for 2 cores
    [5,10,19,37,74,97],  # Throughput for 3 cores
    [7,13,26,50,95,97],   # Throughput for 4 cores
    [9,17,32,59,98,97],   # Throughput for 5 cores
    [11,20,38,75,98,97],   # Throughput for 6 cores
    [12,23,42,80,98,97],   # Throughput for 7 cores
    [12,20,35,71,98,97]   # Throughput for 8 cores
]

# Create a DataFrame for the heatmap and transpose it
data = np.array(throughput_data[::-1])
data = np.array(throughput_data)
df = pd.DataFrame(data.T, index=packet_sizes, columns=cores)
df = df[::-1]

plt.subplot(2, 1, 2)
# fig = plt.figure(figsize=(14, 10))
# plt.rcParams.update({'font.size': 24})
colors = ['#8F493F', '#82AA45']  # Define the colors for the colormap
cmap = LinearSegmentedColormap.from_list('custom', colors, N=256)
ax = sns.heatmap(df, annot=True, cmap=cmap)
# plt.title('Throughput as a function of hash functions and packet size')
cbar = ax.collections[0].colorbar
cbar.set_label('Throughput (Gbps)', rotation=90, labelpad=20)
plt.xlabel('CPU Cores')
plt.ylabel('Packet Sizes (Bytes)')

plt.subplots_adjust(hspace=0.2)  # Increase the vertical space between subplots
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)

plt.savefig("cdf_grid.pdf")
plt.show()
