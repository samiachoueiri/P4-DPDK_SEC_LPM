import csv
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib.colors import LinearSegmentedColormap, Normalize
from matplotlib.ticker import ScalarFormatter

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
fsize = 43
fig = plt.figure(figsize=(27, 13))  # Set the overall figure size
plt.rcParams.update({'font.size': 43}) #16
gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.2])  # Create 1 row and 2 columns grid

# First subplot: Line plot
ax1 = fig.add_subplot(gs[0, 0])  # Place this subplot in the first grid cell
ax1.plot(packet_sizes_mawi, mar_count, label='MAWI 03/15/2024')
ax1.plot(packet_sizes_mawi, oct_count, label='MAWI 11/25/2024')
ax1.plot(packet_sizes_caida, jan1_count, label='CAIDA 01/20/2019')
ax1.plot(packet_sizes_caida, jan2_count, label='CAIDA 01/21/2019')

# ax1.set_xscale('symlog')  # Set x-axis to logarithmic scale
# ax1.xaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ax1.set_xlim(0, 1501)
ax1.set_xticks([64, 128, 256, 512, 1024, 1500])
# ax1.tick_params(axis='x', which='both', bottom=True, top=False, labelbottom=False)  # Hide the tick labels
# ax1.tick_params(axis='x', which='major', length=10)  # Adjust tick length for the grid line
labels = ax1.get_xticklabels()
labels[1].set_visible(False)  # Hide the tick label for 64

ax1.set_xlabel('Packet Size (Bytes) \n (a)')
ax1.set_ylabel('Cumulative Percentage')
ax1.grid(True)
# ax1.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc="lower center", ncol=4, mode="expand", borderaxespad=0., fontsize=30-4)
ax1.legend(bbox_to_anchor=(-0.2, 1.02, 1.2, .102), loc="lower center", ncol=2, mode="expand", borderaxespad=0., fontsize=fsize-4, handlelength=1,labelspacing=0.1)

# ---------------------------------------------------------------------------------------------------------------------------
# Number of cores and packet sizes
ax2 = fig.add_subplot(gs[0, 1])  # Place this subplot in the second grid cell

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
data = np.array(throughput_data[::1])
df = pd.DataFrame(data.T, index=packet_sizes, columns=cores)
df = df[::-1]

colors = ['#8F493F', '#82AA45']  # Define the colors for the colormap
cmap = LinearSegmentedColormap.from_list('custom', colors, N=256)
ax = sns.heatmap(df, annot=True, cmap=cmap, cbar_kws={"shrink": 1})
cbar = ax.collections[0].colorbar
cbar.set_label('Throughput (Gbps)', rotation=90, labelpad=1)
cbar.set_ticks([0, 20, 40, 60, 80, 100])
ax2.tick_params(axis='y', rotation=90)
ax2.set_xlabel('CPU Cores \n (b)')
ax2.set_ylabel('Packet Sizes (Bytes)')

plt.subplots_adjust(wspace=0.15)  # Increase the horizontal space between subplots
plt.subplots_adjust(left=0.1, right=0.9, top=0.9, bottom=0.1)
fig.tight_layout()
plt.savefig("cdf_grid.pdf")
# plt.show()
