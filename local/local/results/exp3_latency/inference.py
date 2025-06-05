import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

mpl.rcParams['font.size'] = 30
fig, ax1 = plt.subplots(figsize=(16, 7.5))

cores = [1, 2, 3, 4, 5, 6, 7, 8]
syn_latency = [1.4,1.2,1,0.8,1.2,0.2,0.8,0.2]
synack_latency = [1.2,1.2,0.4,0.8,1.2,0.2,0.4,0.6]
ack_latency = [1,1,0.4,0.6,0.6,0.8,0.8,0.6]
fin_latency = [0.4,0.4,0.4,0.4,0.8,0.4,0.2,0]
hh_latency = [0.2,0.6,0.6,0.4,0.8,0.4,0.4,0.2]
icmp_latency = [0.2,0.4,0.6,0.6,0.4,0.6,0.4,0.2]
udp_latency = [1.4,0.2,0,0.2,0.2,0.2,0.2,0]

# First y-axis (Latency %)
ax1.plot(cores, syn_latency, marker='o', label='SYN Flood',color="gray")
ax1.plot(cores, synack_latency, marker='s', label='SYN-ACK Flood')
ax1.plot(cores, ack_latency, marker='^', label='ACK Flood')
ax1.plot(cores, fin_latency, marker='D', label='FIN Flood')
ax1.plot(cores, hh_latency, marker='P', label='Heavy Hitter')
ax1.plot(cores, icmp_latency, marker='.', label='ICMP Flood')
ax1.plot(cores, udp_latency, marker='.', label='UDP Flood')

fsize = 30
ax1.set_ylim(-0.1, 5)
ax1.set_xlabel('CPU Cores \n (b)', fontsize=fsize)
ax1.set_xticks(cores)
ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
ax1.set_yticks([0,2,4,6,8,10])
ax1.set_ylabel('Inference time (us)', fontsize=fsize)
ax1.grid(True, linestyle='--')
ax1.set_xlim(0.9, 8)


# # Create a second y-axis for Average Inference Time
# ax2 = ax1.twinx()  # This shares the same x-axis
# avg_inference = [1.142857143, 1.142857143, 1.428571429, 2.214285714, 3.142857143, 5.071428571, 5.489795918, 5.6]
# ax2.plot(cores, avg_inference, marker='X', color='blue', label='Average\nInference Time')

# # Second y-axis (Inference Time in microseconds)
# ax2.set_ylim(0, 10)
# ax2.set_ylabel('Average Inference Time (us)', fontsize=fsize)
# ax2.grid(True, linestyle='--')

# ax2.set_yticks([1, 3, 5 , 6, 10])  # Set the ticks to 3, 4, 5
# ax2.set_yticklabels(['1', '3', '5','6','10'], fontsize=fsize - 1)  # Custom labels for the right y-axis

# # Change the color and thickness of the right y-axis
# ax2.spines['right'].set_color('blue')  # Set the color of the right y-axis
# ax2.spines['right'].set_linewidth(2)  # Set the thickness of the right y-axis line



# Add legends for both axes
ax1.legend(loc='upper left', bbox_to_anchor=(0., 1.27, 1, 0.05), ncol=4, mode="expand", borderaxespad=0., fontsize=fsize - 4, frameon=True, handlelength=1,labelspacing=0.1)
# ax2.legend(loc='upper right', bbox_to_anchor=(0., 0.95, 1., 0.05), ncol=1, fontsize=fsize - 4, borderaxespad=0.1, frameon=True)

plt.tight_layout()
plt.savefig('inference.pdf')
plt.show()
