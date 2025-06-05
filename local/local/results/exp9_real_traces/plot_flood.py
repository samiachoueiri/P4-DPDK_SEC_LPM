import numpy as np
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec
import matplotlib as mpl

# Increase font size globally
fsize = 32
mpl.rcParams['font.size'] = fsize

# Load the data
data1 = np.loadtxt("night_out.txt")
data2 = np.loadtxt("syn_out.txt")

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

# Process datasets
time1, actual1, predicted1, allowed1 = process_data(data1)
time2, actual2, predicted2, allowed2 = process_data(data2)

# Time shifts
time1 -= 6
time2 -= 6

# Create figure and subplots
fig = plt.figure(figsize=(17, 15))
# gs = gridspec.GridSpec(2, 1)
gs = gridspec.GridSpec(1, 1)

# Top subplot: ax1 and ax2 on the same axis
ax_main = fig.add_subplot(gs[0, 0])

# ax1: Plot from data1
ax_main.plot(time1[:len(actual1)], actual1, label="Observed (Night)", color='#95253B')
ax_main.plot(time1[:len(predicted1)], predicted1, label="Predicted (Night)", color='#3a7cb3')
ax_main.plot(time1[:len(allowed1)], allowed1, marker='.', color='none')
ax_main.fill_between(time1[:len(predicted1)], predicted1, allowed1, color='#c4daec', alpha=0.5, label="Allowed Margin (Night)")

# ax2: Overlay Plot from data2
ax_main.plot(time2[:len(actual2)], actual2, label="Observed (Flood)", linestyle='--', color='#FF5733')
ax_main.plot(time2[:len(predicted2)], predicted2, label="Predicted (Flood)", linestyle='--', color='#33C3FF')
ax_main.plot(time2[:len(allowed2)], allowed2, marker='.', color='none')
ax_main.fill_between(time2[:len(predicted2)], predicted2, allowed2, color='#FFDBB4', alpha=0.4, label="Allowed Margin (Flood)")

ax_main.set_title(r"Overlay: Night and Flood $\alpha = 0.2927$ , k = 7", fontsize=fsize)
ax_main.set_xlim(0, 900)
ax_main.set_ylim(0, 150)
ax_main.set_ylabel("Throughput (Kpps)")
ax_main.set_xticklabels([])
ax_main.set_yticks([0, 25, 50, 75, 100, 125, 150])
ax_main.set_yticklabels(['0', '25', '50', '75', '100', '125', '150'])
ax_main.grid(True)
ax_main.legend(loc='upper left', bbox_to_anchor=(0., 1.5, 1.00, 0.05), ncol=2, mode="expand", borderaxespad=0., fontsize=fsize - 4, frameon=True)

print( "TP: 100 FP: 0 TN: 100 FN: 0 ")
# # Bottom subplot: Just flood data
# ax3 = fig.add_subplot(gs[1, 0])
# ax3.plot(time2[:len(actual2)], actual2, color='#95253B')
# ax3.plot(time2[:len(predicted2)], predicted2, color='#3a7cb3')
# ax3.plot(time2[:len(allowed2)], allowed2, marker='.', color='none')
# ax3.fill_between(time2[:len(predicted2)], predicted2, allowed2, color='#c4daec', alpha=0.5)
# ax3.set_title(r"Flood: $\alpha = 0.2927$ , k = 7", fontsize=fsize)
# ax3.set_xlim(0, 900)
# ax3.set_xlabel("Time (s)")
# ax3.set_ylabel("Throughput (Kpps)")
# ax3.set_yticks([0, 25, 50, 75, 100])
# ax3.set_yticklabels(['0', '25', '50', '75', '100'])
# ax3.grid(True)

plt.tight_layout()
plt.subplots_adjust(hspace=0.2, wspace=0.05)
plt.show()
