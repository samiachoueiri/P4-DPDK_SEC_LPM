import matplotlib as mpl
import matplotlib.pyplot as plt
from matplotlib.ticker import MaxNLocator

mpl.rcParams['font.size'] = 30
fig, (ax1,ax2) = plt.subplots(2,1,figsize=(16, 15))

cores = [1, 2, 3, 4, 5, 6, 7, 8]
syn_latency = [374.6,31.34,35.7,40.32,46.28,51.9,55.84,61.12]
synack_latency = [372,32.1,36.14,40.52,46.42,51.7,56.62,62.24]
ack_latency = [382,31.54,36.8,40.6,46.36,51.16,56.36,62.22]
fin_latency = [285.6,33.1,36.76,40.3,46.8,51.8,56.64,61.98]
hh_latency = [368.6,34.02,38.14,42.9,49.58,54.76,60.6,65.54]
icmp_latency = [376.8,32.32,36.56,41,47.7,52.46,58.06,63.44]
udp_latency = [375,32,35.98,40.62,46.28,51.34,56.1,61.22]

# First y-axis (Latency %)
ax1.plot(cores, syn_latency, marker='o', label='SYN Flood',color="gray")
ax1.plot(cores, synack_latency, marker='s', label='SYN-ACK Flood')
ax1.plot(cores, ack_latency, marker='^', label='ACK Flood')
ax1.plot(cores, fin_latency, marker='D', label='FIN Flood')
ax1.plot(cores, hh_latency, marker='P', label='Heavy Hitter')
ax1.plot(cores, icmp_latency, marker='.', label='ICMP Flood')
ax1.plot(cores, udp_latency, marker='.', label='UDP Flood')

fsize = 30
ax1.set_ylim(-5, 400)
ax1.set_xlabel('CPU Cores \n (a)', fontsize=fsize)
ax1.set_xticks(cores)
ax1.yaxis.set_major_locator(MaxNLocator(integer=True))
ax1.set_yticks([0, 50, 100, 200, 300, 400])
ax1.set_ylabel('Latency (us)', fontsize=fsize)
ax1.grid(True, linestyle='--')
ax1.set_xlim(0.9, 8)

# ---------------------------

cores = [1, 2, 3, 4, 5, 6, 7, 8]
syn_latency = [1.4,1.2,1,0.8,1.2,0.2,0.8,0.2]
synack_latency = [1.2,1.2,0.4,0.8,1.2,0.2,0.4,0.6]
ack_latency = [1,1,0.4,0.6,0.6,0.8,0.8,0.6]
fin_latency = [0.4,0.4,0.4,0.4,0.8,0.4,0.2,0]
hh_latency = [0.2,0.6,0.6,0.4,0.8,0.4,0.4,0.2]
icmp_latency = [0.2,0.4,0.6,0.6,0.4,0.6,0.4,0.2]
udp_latency = [1.4,0.2,0,0.2,0.2,0.2,0.2,0]

ax2.plot(cores, syn_latency, marker='o', label='SYN Flood',color="gray")
ax2.plot(cores, synack_latency, marker='s', label='SYN-ACK Flood')
ax2.plot(cores, ack_latency, marker='^', label='ACK Flood')
ax2.plot(cores, fin_latency, marker='D', label='FIN Flood')
ax2.plot(cores, hh_latency, marker='P', label='Heavy Hitter')
ax2.plot(cores, icmp_latency, marker='.', label='ICMP Flood')
ax2.plot(cores, udp_latency, marker='.', label='UDP Flood')

fsize = 30
ax2.set_ylim(-0.1, 2)
ax2.set_xlabel('CPU Cores \n (b)', fontsize=fsize)
ax2.set_xticks(cores)
ax2.yaxis.set_major_locator(MaxNLocator(integer=True))
ax2.set_yticks([0,2,4,6,8,10])
ax2.set_ylabel('Inference time (us)', fontsize=fsize)
ax2.grid(True, linestyle='--')
ax2.set_xlim(0.9, 8)


# Add legends for both axes
ax1.legend(loc='upper left', bbox_to_anchor=(0., 1.27, 1, 0.05), ncol=4, mode="expand", borderaxespad=0., fontsize=fsize - 4, frameon=True, handlelength=1,labelspacing=0.1)
# ax2.legend(loc='upper right', bbox_to_anchor=(0., 0.95, 1., 0.05), ncol=1, fontsize=fsize - 4, borderaxespad=0.1, frameon=True)

plt.tight_layout()
# plt.savefig('latency_inf.pdf')
plt.show()
