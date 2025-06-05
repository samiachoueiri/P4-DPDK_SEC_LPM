import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

# Increase font size globally
mpl.rcParams['font.size'] = 30
# fig, ax1 = plt.subplots(figsize=(17, 10))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(17, 10))
# gs = fig.add_gridspec(1, 2, width_ratios=[1, 1])  # Create 1 row and 2 columns grid

cores = [1, 2, 3, 4, 5, 6, 7, 8]
syn_loss = [83.73988397,74.41002046,64.33377859,57.98662162,46.13696131,43.43654445,37.24434744,29.46283657]
# synack_loss = [73.23, 48.79, 19.94, 1.78, 0.2921, 0.1954, 0.2751, 0]
# ack_loss = [73.799, 48.09, 21.65, 0.4154, 0.199, 0.1272, 0.3598, 0]
fin_loss = [85.99371371,76.99162727,63.20297711,54.47663533,49.25893145,42.6180939,38.70577385,27.66622025]
hh_loss = [80.98188454,71.95574815,59.67107091,51.03757543,47.5570505,40.25060542,30.34395486,28.48323137]
icmp_loss = [86.28461587,76.08462462,65.01948951,57.2363874,49.69703858,41.6762875,37.66422746,37.12124427]
udp_loss = [84.83439114,77.32983315,67.7594251,54.27446028,46.2437883,41.7028622,40.41391481,36.12285278]

# First y-axis (Loss %)
ax1.plot(cores, syn_loss, marker='o', label='TCP Flood',color="gray")
# ax1.plot(cores, synack_loss, marker='s', label='SYN-ACK Flood')
# ax1.plot(cores, ack_loss, marker='^', label='ACK Flood')
# ax1.plot(cores, fin_loss, marker='D', label='FIN Flood')
ax1.plot(cores, hh_loss, marker='P', label='Heavy Hitter')
ax1.plot(cores, icmp_loss, marker='.', label='ICMP Flood')
ax1.plot(cores, udp_loss, marker='.', label='UDP Flood')

fsize = 30
ax1.set_ylim(-5, 100)
ax1.set_title('Suricata DPDK',fontsize=fsize-2)
ax1.set_xlabel('CPU Cores \n (a)', fontsize=fsize)
ax1.set_xticks(cores)
# ax1.set_yticklabels([-5, 0, 20, 40, 60, 80, 100], fontsize=fsize - 1)
ax1.set_yticks([0, 25, 50, 75, 100])
ax1.set_ylabel('Loss (%)', fontsize=fsize)
ax1.grid(True, linestyle='--')
ax1.set_xlim(0.9, 8)

# Add legends for both axes
ax1.legend(loc='upper left', bbox_to_anchor=(0., 1.125, 2.25, 0.05), ncol=4, mode="expand", borderaxespad=0., fontsize=fsize - 4,labelspacing=0.3, frameon=True)
# ax1.legend(loc='upper left', bbox_to_anchor=(0., 1.09, 0.75, 0.05), ncol=4, mode="expand", borderaxespad=0., fontsize=fsize - 4,labelspacing=0.3, frameon=True)

# # ---------------------------------------------------------------------------------------------------------------------------
# ax2 = fig.add_subplot(gs[0, 1])  # Place this subplot in the second grid cell

cores = [1, 2, 3, 4, 5, 6, 7, 8]
syn_loss = [74.35, 48.45, 20.21, 0.4783, 0.0335, 0.0329, 0.041, 0]
synack_loss = [73.23, 48.79, 19.94, 1.78, 0.2921, 0.1954, 0.2751, 0]
ack_loss = [73.799, 48.09, 21.65, 0.4154, 0.199, 0.1272, 0.3598, 0]
fin_loss = [74.15, 49.76, 20.76, 0.7026, 0.1544, 0.1609, 0.0637, 0]
hh_loss = [71.88, 44.44, 15.45, 0.0855, 0.0149, 0.1887, 0.046, 0]
icmp_loss = [73.97985786, 45.73825349, 17.1465451, 1.27843179, 0.074633319, 0.060794753, 0.064797723, 0]
udp_loss = [75.87832757, 47.998298, 20.89101077, 2.280879384, 0.100966063, 0.464010086, 0.010073463, 0]

# First y-axis (Loss %)
# ax2 = fig.add_subplot(gs[0, 0])  # Place this subplot in the first grid cell
ax2.plot(cores, syn_loss, marker='o', label='TCP Flood',color="gray")
# ax2.plot(cores, synack_loss, marker='s', label='SYN-ACK Flood')
# ax2.plot(cores, ack_loss, marker='^', label='ACK Flood')
# ax2.plot(cores, fin_loss, marker='D', label='FIN Flood')
ax2.plot(cores, hh_loss, marker='P', label='Heavy Hitter')
ax2.plot(cores, icmp_loss, marker='.', label='ICMP Flood')
ax2.plot(cores, udp_loss, marker='.', label='UDP Flood')

fsize = 30
ax2.set_ylim(-5, 100)
ax2.set_title('Proposed System',fontsize=fsize-2)
ax2.set_xlabel('CPU Cores \n (b)', fontsize=fsize)
ax2.set_xticks(cores)
ax2.set_yticklabels([-5, 0, 20, 40, 60, 80, 100], fontsize=fsize - 1)
ax2.set_ylabel('Loss (%)', fontsize=fsize)
ax2.grid(True, linestyle='--')
ax2.set_xlim(0.9, 8)


# Add legends for both axes
# ax2.legend(loc='upper left', bbox_to_anchor=(0., 1.05, 1, 0.05), ncol=5, mode="expand", borderaxespad=0.05, fontsize=fsize - 4,handlelength=1,labelspacing=0.05, frameon=True)


plt.tight_layout()

# plt.savefig('loss_cores.pdf')

# Show the plot
plt.show()
