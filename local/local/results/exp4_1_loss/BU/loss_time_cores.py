import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Increase font size globally
mpl.rcParams['font.size'] = 30
fig, ax1 = plt.subplots(figsize=(17, 10))

cores = [1, 2, 3, 4, 5, 6, 7, 8]
syn_loss = [74.35, 48.45, 20.21, 0.4783, 0.0335, 0.0329, 0.041, 0]
synack_loss = [73.23, 48.79, 19.94, 1.78, 0.2921, 0.1954, 0.2751, 0]
ack_loss = [73.799, 48.09, 21.65, 0.4154, 0.199, 0.1272, 0.3598, 0]
fin_loss = [74.15, 49.76, 20.76, 0.7026, 0.1544, 0.1609, 0.0637, 0]
hh_loss = [71.88, 44.44, 15.45, 0.0855, 0.0149, 0.1887, 0.046, 0]
icmp_loss = [73.97985786, 45.73825349, 17.1465451, 1.27843179, 0.074633319, 0.060794753, 0.064797723, 0]
udp_loss = [75.87832757, 47.998298, 20.89101077, 2.280879384, 0.100966063, 0.464010086, 0.010073463, 0]

# First y-axis (Loss %)
ax1.plot(cores, syn_loss, marker='o', label='SYN Flood',color="gray")
ax1.plot(cores, synack_loss, marker='s', label='SYN-ACK Flood')
ax1.plot(cores, ack_loss, marker='^', label='ACK Flood')
ax1.plot(cores, fin_loss, marker='D', label='FIN Flood')
ax1.plot(cores, hh_loss, marker='P', label='Heavy Hitter')
ax1.plot(cores, icmp_loss, marker='.', label='ICMP Flood')
ax1.plot(cores, udp_loss, marker='.', label='UDP Flood')

fsize = 30
ax1.set_ylim(-5, 100)
ax1.set_xlabel('CPU Cores', fontsize=fsize)
ax1.set_xticks(cores)
ax1.set_yticklabels([-5, 0, 20, 40, 60, 80, 100], fontsize=fsize - 1)
ax1.set_ylabel('Loss (%)', fontsize=fsize)
ax1.grid(True, linestyle='--')
ax1.set_xlim(0.9, 8)

# Create a second y-axis for Average Inference Time
ax2 = ax1.twinx()  # This shares the same x-axis
avg_inference = [1.142857143, 1.142857143, 1.428571429, 2.214285714, 3.142857143, 5.071428571, 5.489795918, 5.6]
ax2.plot(cores, avg_inference, marker='X', color='blue', label='Average\nInference Time')

# Second y-axis (Inference Time in microseconds)
ax2.set_ylim(0, 10)
ax2.set_ylabel('Average Inference Time (us)', fontsize=fsize)
ax2.grid(True, linestyle='--')

ax2.set_yticks([1, 1.5, 3, 5 , 6, 10])  # Set the ticks to 3, 4, 5
ax2.set_yticklabels(['1', '1.5', '3', '5','6','10'], fontsize=fsize - 1)  # Custom labels for the right y-axis

# Change the color and thickness of the right y-axis
ax2.spines['right'].set_color('blue')  # Set the color of the right y-axis
ax2.spines['right'].set_linewidth(2)  # Set the thickness of the right y-axis line

# Add legends for both axes
ax1.legend(loc='upper left', bbox_to_anchor=(0., 1.125, 1, 0.05), ncol=4, mode="expand", borderaxespad=0., fontsize=fsize - 4,labelspacing=0.3, frameon=True)
# ax1.legend(loc='upper left', bbox_to_anchor=(0., 1.09, 0.75, 0.05), ncol=4, mode="expand", borderaxespad=0., fontsize=fsize - 4,labelspacing=0.3, frameon=True)
ax2.legend(loc='upper right', bbox_to_anchor=(0., 0.95, 1., 0.05), ncol=1, fontsize=fsize - 4, borderaxespad=0.1, frameon=True)

plt.tight_layout()

# plt.savefig('loss_time_cores.pdf')
# plt.savefig('packet_loss.png')

# Show the plot
plt.show()
