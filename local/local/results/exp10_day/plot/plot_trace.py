import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Increase font size globally
fsize = 28
mpl.rcParams['font.size'] = fsize

# Load and process data1
data1 = np.loadtxt("5min_flood_out.txt")
data2 = np.loadtxt("day_flood_20240619_12_out.txt")
data3 = np.loadtxt("day_flood_20250409_out.txt")

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

time1, actual1, predicted1, allowed1 = process_data(data1)
last_5_actual = actual1[-5:]
last_5_predicted = predicted1[-5:]
last_5_allowed = allowed1[-5:]
actual1 = np.concatenate((actual1, last_5_actual, last_5_actual))
predicted1 = np.concatenate((predicted1, last_5_predicted, last_5_predicted))
allowed1 = np.concatenate((allowed1, last_5_allowed, last_5_allowed))
time1 = list(range(len(actual1)))
time1 = [i / 60 for i in range(len(actual1))]
xtickss = range(0, int(time1[-1]) + 1, 1)
time_o = [(i-1)/ 60 for i in range(len(actual1))]


time2, actual2, predicted2, allowed2 = process_data(data2)
last_20_actual = actual2[-20:]
last_20_predicted = predicted2[-20:]
last_20_allowed = allowed2[-20:]
actual2 = np.concatenate((actual2, last_20_actual, last_20_actual))
predicted2 = np.concatenate((predicted2, last_20_predicted, last_20_predicted))
allowed2 = np.concatenate((allowed2, last_20_allowed, last_20_allowed))
time2 = list(range(len(actual2)))
time2 = [i / 3600 for i in range(len(actual2))]
xtickshh = range(0, int(time2[-1]) + 1, 1)
time_o2 = [(i-1)/ 3600 for i in range(len(actual2))]

time3, actual3, predicted3, allowed3 = process_data(data3)
last_900_actual = actual3[-900:]
last_900_predicted = predicted3[-900:]
last_900_allowed = allowed3[-900:]
actual3 = np.concatenate((actual3, last_900_actual, last_900_actual))
predicted3 = np.concatenate((predicted3, last_900_predicted, last_900_predicted))
allowed3 = np.concatenate((allowed3, last_900_allowed, last_900_allowed))
time3 = list(range(len(actual3)))
time3 = [i / 3600 for i in range(len(actual3))]
xticksh = range(0, int(time3[-1]) + 1, 1)
time_o3 = [(i-1)/ 3600 for i in range(len(actual3))]

fig, (ax1, ax2, ax3 )= plt.subplots(3,1, figsize=(17, 17))

mean_data1 = 27.49
mean_data2 = 16.11
mean_data3 = 17.15
std_data1 = 1.07
std_data2 = 1.65
std_data3 = 2.75

# Plot
ax1.plot(time_o[:len(actual1)], actual1, label="Observed", color='#95253B')
ax1.plot(time1[:len(predicted1)], predicted1, label="Predicted", color='#3a7cb3')
ax1.plot(time1[:len(allowed1)], allowed1, marker='.', color='none')  # invisible markers
ax1.fill_between(time1[:len(predicted1)], predicted1, allowed1, color='#c4daec', alpha=0.5, label="Allowed Margin")
# Formatting
ax1.set_title(r"Caida: January 17 2019", fontsize=fsize)
ax1.set_xlim(0, 4.8)
# ax1.set_ylim(0, 100)
ax1.set_xlabel("Time (m)")
# ax1.set_ylabel("Throughput (Kpps)")
ax1.set_xticks(xtickss)
ax1.set_ylabel("Throughput (Kpps)")
# ax1.set_yticks([0, 25, 50, 75, 100])
# ax1.set_yticklabels(['0', '25', '50', '75', '100'])
ax1.grid(True)
ax1.legend(loc='upper left', bbox_to_anchor=(0., 1.5, 1, 0.05), ncol=4, mode="expand", borderaxespad=0., fontsize=fsize - 4, frameon=True, handlelength=2,labelspacing=0.1)
# ax1.legend(loc='upper left', fontsize=fsize - 2, frameon=True)
# ax1.set_yscale('log')

# Add text box with mean (μ) and standard deviation (σ) to Signal 1
stats_text1 = f"μ: {mean_data1:.2f}\nσ: {std_data1:.2f}"
ax1.text(0.9, 0.9, stats_text1, transform=ax1.transAxes, fontsize=25,
         verticalalignment='top', horizontalalignment='right',
         bbox=dict(facecolor='white', alpha=0.7, edgecolor='black', boxstyle='round,pad=0.5'))

# Plot
ax2.plot(time_o2[:len(actual2)], actual2, label="Observed", color='#95253B')
ax2.plot(time2[:len(predicted2)], predicted2, label="Predicted", color='#3a7cb3')
ax2.plot(time2[:len(allowed2)], allowed2, marker='.', color='none')  # invisible markers
ax2.fill_between(time2[:len(predicted2)], predicted2, allowed2, color='#c4daec', alpha=0.5, label="Allowed Margin")
# Formatting
ax2.set_title(r"Mawi: June 19 2024", fontsize=fsize)
ax2.set_xlim(0, 12)
# ax2.set_ylim(0, 100)
ax2.set_xlabel("Time (h)")
ax2.set_ylabel("Throughput (Kpps)")
ax2.set_xticks(xtickshh)
# ax2.set_yticks([0, 25, 50, 75, 100])
# ax2.set_yticklabels(['0', '25', '50', '75', '100'])
ax2.grid(True)
# ax2.legend(loc='upper left', fontsize=fsize - 2, frameon=True)
# ax1.set_yscale('log')

# Add text box with mean (μ) and standard deviation (σ) to Signal 1
stats_text2 = f"μ: {mean_data2:.2f}\nσ: {std_data2:.2f}"
ax2.text(0.9, 0.9, stats_text2, transform=ax2.transAxes, fontsize=25,
         verticalalignment='top', horizontalalignment='right',
         bbox=dict(facecolor='white', alpha=0.7, edgecolor='black', boxstyle='round,pad=0.5'))

# Plot
ax3.plot(time_o3[:len(actual3)], actual3, label="Observed", color='#95253B')
ax3.plot(time3[:len(predicted3)], predicted3, label="Predicted", color='#3a7cb3')
ax3.plot(time3[:len(allowed3)], allowed3, marker='.', color='none')  # invisible markers
ax3.fill_between(time3[:len(predicted3)], predicted3, allowed3, color='#c4daec', alpha=0.5, label="Allowed Margin")
# Formatting
ax3.set_title(r"Mawi: April 09 2025", fontsize=fsize)
ax3.set_xlim(0, 24)
# ax3.set_ylim(0, 100)
ax3.set_xlabel("Time (h)")
# ax3.set_ylabel("Throughput (Kpps)")
ax3.set_xticks(xticksh)
ax3.set_ylabel("Throughput (Kpps)")
# ax3.set_yticks([0, 25, 50, 75, 100])
# ax3.set_yticklabels(['0', '25', '50', '75', '100'])
ax3.grid(True)
# ax3.legend(loc='upper left', fontsize=fsize - 2, frameon=True)

# Add text box with mean (μ) and standard deviation (σ) to Signal 1
stats_text3 = f"μ: {mean_data3:.2f}\nσ: {std_data3:.2f}"
ax3.text(0.9, 0.9, stats_text3, transform=ax3.transAxes, fontsize=25,
         verticalalignment='top', horizontalalignment='right',
         bbox=dict(facecolor='white', alpha=0.7, edgecolor='black', boxstyle='round,pad=0.5'))

plt.subplots_adjust(hspace=0.50)  # Adjust this value to control vertical spacing
plt.savefig('real_data.pdf')
# plt.tight_layout(h_pad=0.7)
# plt.show()
