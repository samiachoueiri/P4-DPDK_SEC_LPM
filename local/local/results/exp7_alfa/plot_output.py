import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib as mpl

# Increase font size globally
fsize = 32
mpl.rcParams['font.size'] = fsize

# Load the data from each file
data1 = np.loadtxt("output_005.txt")
data2 = np.loadtxt("output_010.txt")
data3 = np.loadtxt("output_025.txt")
data4 = np.loadtxt("output_050.txt")

def process_data(data):
    time = data[:, 0]
    actual = data[:, 3] / 1000
    predicted = data[:, 4] / 1000
    allowed = data[:, 5] / 1000
    return (
        time[:-1],
        actual[:-1],
        predicted[1:],
        allowed[1:]
    )

# Process each dataset
time1, actual1, predicted1, allowed1 = process_data(data1)
time2, actual2, predicted2, allowed2 = process_data(data2)
time3, actual3, predicted3, allowed3 = process_data(data3)
time4, actual4, predicted4, allowed4 = process_data(data4)

# Apply x-axis time shifts
time1 -= 13
time2 -= 3
time3 -= 8
time4 -= 1

# Create a figure with GridSpec
fig = plt.figure(figsize=(17, 10))
# Create a 2x2 grid with row height ratio of 1 (top) to 2 (bottom)
gs = gridspec.GridSpec(2, 2, height_ratios=[1, 1])

# Subplots
ax1 = fig.add_subplot(gs[0, 0])  # Top-left (shorter height)
ax2 = fig.add_subplot(gs[0, 1])  # Top-right (shorter height)
ax3 = fig.add_subplot(gs[1, 0])  # Bottom-left (taller height)
ax4 = fig.add_subplot(gs[1, 1])  # Bottom-right (taller height)
# Plot 1
ax1.plot(time1[:len(actual1)], actual1, label="Observed", color='#95253B',linewidth=2)
ax1.plot(time1[:len(predicted1)], predicted1, label="Predicted", color='#3a7cb3',linewidth=2)
# ax1.plot(time1[:len(allowed1)], allowed1, marker='.', label="Allowed", color='#3a7cb3')
ax1.plot(time1[:len(allowed1)], allowed1, marker='.', color='none',linewidth=2)
ax1.fill_between(time1[:len(predicted1)], predicted1, allowed1, color='#c4daec', alpha=0.5, label="Allowed Margin")
ax1.set_title(r"$\alpha = 0.05$", fontsize=27)
ax1.set_xlim(0, 30)
ax1.set_ylim(75, 210)
# ax1.set_ylabel("Throughput (Kpps)")
# ax1.set_ylabel("Throughput (Thousand Packets per Second)")
ax1.set_xticklabels([])
ax1.set_yticks([80, 100, 150, 200])
ax1.set_yticklabels(['80', '100', '150', '200'])
ax1.grid(True)
ax1.legend(loc="upper right")
ax1.legend(loc='upper left', bbox_to_anchor=(0., 1.6, 2.05, 0.05), ncol=4, mode="expand", borderaxespad=0., fontsize=fsize - 2,labelspacing=0.3, frameon=True)

# Plot 2
ax2.plot(time2[:len(actual2)], actual2, color='#95253B',linewidth=2)
ax2.plot(time2[:len(predicted2)], predicted2, color='#3a7cb3',linewidth=2)
# ax2.plot(time2[:len(allowed2)], allowed2, marker='.', color='#3a7cb3')
ax2.plot(time2[:len(allowed2)], allowed2, marker='.', color='none',linewidth=2)
ax2.fill_between(time2[:len(predicted2)], predicted2, allowed2, color='#c4daec', alpha=0.5)
ax2.set_title(r"$\alpha = 0.1$", fontsize=27)
ax2.set_xlim(0, 30)
ax2.set_ylim(75, 210)
ax2.set_xticklabels([])
ax2.set_yticks([80, 100, 150, 200])
ax2.set_yticklabels([])
ax2.grid(True)

# Plot 3
ax3.plot(time3[:len(actual3)], actual3, color='#95253B',linewidth=2)
ax3.plot(time3[:len(predicted3)], predicted3, color='#3a7cb3',linewidth=2)
# ax3.plot(time3[:len(allowed3)], allowed3, marker='.', color='#3a7cb3')
ax3.plot(time3[:len(allowed3)], allowed3, marker='.', color='none',linewidth=2)
ax3.fill_between(time3[:len(predicted3)], predicted3, allowed3, color='#c4daec', alpha=0.5)
ax3.set_title(r"$\alpha = 0.25$", fontsize=27)
ax3.set_xlim(0, 30)
ax3.set_ylim(75, 210)
ax3.set_yticks([80, 100, 150, 200])
ax3.set_yticklabels(['80', '100', '150', '200'])
ax3.set_xlabel("Time (s)")
# ax3.set_ylabel("Throughput (Thousand Packets per Second)")
ax3.set_ylabel("Throughput (Kpps)")
ax3.grid(True)

# Plot 4
ax4.plot(time4[:len(actual4)], actual4, color='#95253B',linewidth=2)
ax4.plot(time4[:len(predicted4)], predicted4, color='#3a7cb3',linewidth=2)
# ax4.plot(time4[:len(allowed4)], allowed4, marker='.', color='#3a7cb3')
ax4.plot(time4[:len(allowed4)], allowed4, marker='.', color='none',linewidth=2)
ax4.fill_between(time4[:len(predicted4)], predicted4, allowed4, color='#c4daec', alpha=0.5)
ax4.set_title(r"$\alpha = 0.5$", fontsize=27)
ax4.set_xlim(0, 30)
ax4.set_ylim(75, 210)
ax4.set_yticks([80, 100, 150, 200])
ax4.set_xlabel("Time (s)")
ax4.set_yticklabels([])
ax4.grid(True)

plt.tight_layout()
# plt.tight_layout(pad=0.2)  # Smaller pad reduces spacing between subplots
plt.subplots_adjust(hspace=0.2, wspace=0.05)  # Decrease values to reduce space
# plt.savefig("alpha.pdf")
plt.show()
