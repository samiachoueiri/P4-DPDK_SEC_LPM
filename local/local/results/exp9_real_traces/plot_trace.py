import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib as mpl

# Increase font size globally
fsize = 32
mpl.rcParams['font.size'] = fsize

# Load the data from each file
data1 = np.loadtxt("morning_out.txt")
data2 = np.loadtxt("noon_out.txt")
data3 = np.loadtxt("night_out.txt")
# data4 = np.loadtxt("output_050.txt")

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
# time4, actual4, predicted4, allowed4 = process_data(data4)

# Apply x-axis time shifts
time1 -= 6
time2 -= 6
time3 -= 6
# time4 -= 1

# Create a figure with GridSpec
fig = plt.figure(figsize=(17, 15))
# Create a 2x2 grid with row height ratio of 1 (top) to 2 (bottom)
gs = gridspec.GridSpec(3, 1)

# Subplots
ax1 = fig.add_subplot(gs[0, 0])  # Top-left (shorter height)
ax2 = fig.add_subplot(gs[1, 0])  # Top-right (shorter height)
ax3 = fig.add_subplot(gs[2, 0])  # Bottom-left (taller height)
# ax4 = fig.add_subplot(gs[1, 1])  # Bottom-right (taller height)

# Plot 1
ax1.plot(time1[:len(actual1)], actual1, label="Observed", color='#95253B')
ax1.plot(time1[:len(predicted1)], predicted1, label="Predicted", color='#3a7cb3')
# ax1.plot(time1[:len(allowed1)], allowed1, marker='.', label="Allowed", color='#3a7cb3')
ax1.plot(time1[:len(allowed1)], allowed1, marker='.', color='none')
ax1.fill_between(time1[:len(predicted1)], predicted1, allowed1, color='#c4daec', alpha=0.5, label="Allowed Margin")
ax1.set_title(r"Morning: $\alpha = 0.1904$ , k = 6", fontsize=32)
ax1.set_xlim(0, 900)
ax1.set_ylim(0, 100)
# ax1.set_ylabel("Throughput (Kpps)")
# ax1.set_ylabel("Throughput (Thousand Packets per Second)")
ax1.set_xticklabels([])
ax1.set_yticks([0, 25, 50, 75, 100])
ax1.set_yticklabels(['0', '25', '50', '75', '100'])
ax1.grid(True)
ax1.legend(loc="upper right")
ax1.legend(loc='upper left', bbox_to_anchor=(0., 1.6, 1.00, 0.05), ncol=4, mode="expand", borderaxespad=0., fontsize=fsize - 2,labelspacing=0.3, frameon=True)

# Plot 2
ax2.plot(time2[:len(actual2)], actual2, color='#95253B')
ax2.plot(time2[:len(predicted2)], predicted2, color='#3a7cb3')
# ax2.plot(time2[:len(allowed2)], allowed2, marker='.', color='#3a7cb3')
ax2.plot(time2[:len(allowed2)], allowed2, marker='.', color='none')
ax2.fill_between(time2[:len(predicted2)], predicted2, allowed2, color='#c4daec', alpha=0.5)
ax2.set_title(r"Noon: $\alpha = 0.3416$ , k = 8", fontsize=32)
ax2.set_xlim(0, 900)
ax2.set_ylim(0, 100)
ax2.set_xticklabels([])
ax2.set_ylabel("Throughput (Kpps)")
ax2.set_yticks([0, 25, 50, 75, 100])
ax2.set_yticklabels(['0', '25', '50', '75', '100'])
ax2.grid(True)

# Plot 3
ax3.plot(time3[:len(actual3)], actual3, color='#95253B')
ax3.plot(time3[:len(predicted3)], predicted3, color='#3a7cb3')
# ax3.plot(time3[:len(allowed3)], allowed3, marker='.', color='#3a7cb3')
ax3.plot(time3[:len(allowed3)], allowed3, marker='.', color='none')
ax3.fill_between(time3[:len(predicted3)], predicted3, allowed3, color='#c4daec', alpha=0.5)
ax3.set_title(r"Night: $\alpha = 0.2927$ , k = 7", fontsize=32)
ax3.set_xlim(0, 900)
ax3.set_ylim(0, 100)
ax3.set_xlabel("Time (s)")
ax3.set_yticks([0, 25, 50, 75, 100])
ax3.set_yticklabels(['0', '25', '50', '75', '100'])
ax3.grid(True)

# # Plot 4
# ax4.plot(time4[:len(actual4)], actual4, color='#95253B')
# ax4.plot(time4[:len(predicted4)], predicted4, color='#3a7cb3')
# # ax4.plot(time4[:len(allowed4)], allowed4, marker='.', color='#3a7cb3')
# ax4.plot(time4[:len(allowed4)], allowed4, marker='.', color='none')
# ax4.fill_between(time4[:len(predicted4)], predicted4, allowed4, color='#c4daec', alpha=0.5)
# ax4.set_title(r"$\alpha = 0.5$", fontsize=27)
# ax4.set_xlim(0, 30)
# ax4.set_ylim(75, 210)
# ax4.set_xlabel("Time (s)")
# ax4.set_yticklabels([])
# ax4.grid(True)

plt.tight_layout()
# plt.tight_layout(pad=0.2)  # Smaller pad reduces spacing between subplots
plt.subplots_adjust(hspace=0.2, wspace=0.05)  # Decrease values to reduce space
# plt.savefig("mawi.pdf")
plt.show()
