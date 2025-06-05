import matplotlib as mpl
import matplotlib.pyplot as plt

# Increase font size globally
mpl.rcParams['font.size'] = 20
fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(18, 8))

cores = [1,2,3,4,5,6,7,8]
syn_loss = [74.35,48.45,20.21,0.4783,0.0335,0.0329,0.041,0]
synack_loss = [73.23,48.79,19.94,1.78,0.2921,0.1954,0.2751,0]
ack_loss = [73.799,48.09,21.65,0.4154,0.199,0.1272,0.3598,0]
fin_loss = [74.15,49.76,20.76,0.7026,0.1544,0.1609,0.0637,0]
hh_loss = [71.88,44.44,15.45,0.0855,0.0149,0.1887,0.046,0]
icmp_loss = [73.97985786,45.73825349,17.1465451,1.27843179,0.074633319,0.060794753,0.064797723,0]
udp_loss = [75.87832757,47.998298,20.89101077,2.280879384,0.100966063,0.464010086,0.010073463,0]

ax1.plot(cores, syn_loss, marker='o', label='SYN Flood')
ax1.plot(cores, synack_loss, marker='s', label='SYN-ACK Flood')
ax1.plot(cores, ack_loss, marker='^', label='ACK Flood')
ax1.plot(cores, fin_loss, marker='D', label='FIN Flood')
ax1.plot(cores, hh_loss, marker='P', label='Heavy Hitter')
ax1.plot(cores, icmp_loss, marker='.', label='ICMP Flood')
ax1.plot(cores, udp_loss, marker='.', label='UDP Flood')

fsize = 24
# ax1.set_title('Suricata DPDK',fontsize=fsize+2)
ax1.set_ylim(-5, 100)
ax1.set_xlabel('CPU Cores',fontsize=fsize)
ax1.set_xticks(cores)
ax1.set_yticklabels([-5,0,20,40,60,80,100],fontsize=fsize-1)
ax1.set_ylabel('Loss (%)',fontsize=fsize)
ax1.grid(True, linestyle='--')

cores = [1,2,3,4,5,6,7,8]
avg_inference = [1.142857143,1.142857143,1.428571429,2.214285714,3.142857143,5.071428571,5.489795918,0]

ax2.plot(cores, avg_inference, marker='o', label='SYN Flood')

# ax2.set_title('P4-DPDK',fontsize=fsize+2)
ax2.set_ylim(0, 10)
ax2.set_xlabel('CPU Cores',fontsize=fsize)
ax2.set_xticks(cores)
ax2.set_xlim(0.5, 7)
# ax2.set_yticklabels([-5,0,20,40,60,80,100],fontsize=fsize-1)
ax2.set_ylabel('Average Inference Time (us)',fontsize=fsize)
ax2.grid(True, linestyle='--')

ax1.legend(bbox_to_anchor=(0., 1.1, 2.2, 0.05), loc="upper center", ncol=6, mode="expand", borderaxespad=0.,fontsize=fsize-4,frameon=True)
# plt.savefig('packet_loss.pdf')
# plt.savefig('packet_loss.png')
plt.show()

