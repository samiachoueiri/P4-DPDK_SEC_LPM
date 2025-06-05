import matplotlib as mpl
import matplotlib.pyplot as plt

mpl.rcParams['font.size'] = 30
fig, ax1 = plt.subplots(figsize=(16, 10))

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
ax1.plot(cores, fin_loss, marker='D', label='FIN Flood')
ax1.plot(cores, hh_loss, marker='P', label='Heavy Hitter')
ax1.plot(cores, icmp_loss, marker='.', label='ICMP Flood')
ax1.plot(cores, udp_loss, marker='.', label='UDP Flood')

fsize = 30
ax1.set_ylim(-5, 100)
ax1.set_xlabel('CPU Cores', fontsize=fsize)
ax1.set_xticks(cores)
# ax1.set_yticklabels([-5, 0, 20, 40, 60, 80, 100], fontsize=fsize - 1)
ax1.set_yticks([0, 25, 50, 75, 100])
ax1.set_ylabel('Loss (%)', fontsize=fsize)
ax1.grid(True, linestyle='--')
ax1.set_xlim(0.9, 8)

# Add legends for both axes
ax1.legend(loc='upper left', bbox_to_anchor=(0., 1.05, 1, 0.05), ncol=5, mode="expand", borderaxespad=0.05, fontsize=fsize - 4,handlelength=1,labelspacing=0.05, frameon=True)
plt.tight_layout()
# plt.savefig('suricata_loss_cores.pdf')

# Show the plot
plt.show()
