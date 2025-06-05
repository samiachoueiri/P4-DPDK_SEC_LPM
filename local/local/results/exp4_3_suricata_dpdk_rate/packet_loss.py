import matplotlib as mpl
import matplotlib.pyplot as plt

# Increase font size globally
mpl.rcParams['font.size'] = 20
fig, (ax1, ax2) = plt.subplots(1, 2,figsize=(18, 8))


s_rate64 = [1,5,10]
s_rate128 = [1,5,10,25]
s_rate256 = [1,5,10,25,50]
s_rate512 = [1,5,10,25,50,100]
s_rate1024 = [1,5,10,25,50,100]
s_rate1500 = [1,5,10,25,50,100]

s_loss64 = [0.05025,0.6515,0.8119]
s_loss128 = [0.0081,0.3452,0.6772,0.861]
s_loss256 = [0.001,0.1344,0.6147,0.8259,0.9246]
s_loss512 = [0.0146,0.0529,0.0513,0.4757,0.7346,0.8662]
s_loss1024 = [0.0041,0.0081,0.016,0.006,0.4065,0.7167]
s_loss1500 = [0.006,0,0,0.007,0.2387,0.626]

p_rate64 = [1,5,10]
p_rate128 = [1,5,10,25]
p_rate256 = [1,5,10,25,50]
p_rate512 = [1,5,10,25,50,100]
p_rate1024 = [1,5,10,25,50,100]
p_rate1500 = [1,5,10,25,50,100]

p_loss64 = [0,0,0.2316]
p_loss128 = [0,0,0,0.4315]
p_loss256 = [0,0,0,0,0.5]
p_loss512 = [0,0,0,0,0,0.4985]
p_loss1024 = [0,0,0,0,0,0.064]
p_loss1500 = [0,0,0,0,0,0.0356]

s_loss64 = [x * 100 for x in s_loss64]
s_loss128 = [x * 100 for x in s_loss128]
s_loss256 = [x * 100 for x in s_loss256]
s_loss512 = [x * 100 for x in s_loss512]
s_loss1024 = [x * 100 for x in s_loss1024]
s_loss1500 = [x * 100 for x in s_loss1500]
p_loss64 = [x * 100 for x in p_loss64]
p_loss128 = [x * 100 for x in p_loss128]
p_loss256 = [x * 100 for x in p_loss256]
p_loss512 = [x * 100 for x in p_loss512]
p_loss1024 = [x * 100 for x in p_loss1024]
p_loss1500 = [x * 100 for x in p_loss1500]

ax1.plot(s_rate64, s_loss64, marker='o', label='64 Bytes')
ax1.plot(s_rate128, s_loss128, marker='s', label='128 Bytes')
ax1.plot(p_rate256, s_loss256, marker='^', label='256 Bytes')
ax1.plot(p_rate512, s_loss512, marker='D', label='512 Bytes')
ax1.plot(p_rate1024, s_loss1024, marker='P', label='1024 Bytes')
ax1.plot(p_rate1500, s_loss1500, marker='.', label='1500 Bytes')

fsize = 24
ax1.set_title('Suricata DPDK',fontsize=fsize+2)
ax1.set_ylim(-5, 100)
ax1.set_xlabel('Rate (Gbps)',fontsize=fsize)
ax1.set_xticks(s_rate1500)
ax1.set_yticklabels([-5,0,20,40,60,80,100],fontsize=fsize-1)
ax1.set_ylabel('Loss (%)',fontsize=fsize)
ax1.grid(True, linestyle='--')

ax2.plot(p_rate64, p_loss64, marker='o', label='64 Bytes')
ax2.plot(p_rate128, p_loss128, marker='s', label='128 Bytes')
ax2.plot(p_rate256, p_loss256, marker='^', label='256 Bytes')
ax2.plot(p_rate512, p_loss512, marker='D', label='512 Bytes')
ax2.plot(p_rate1024, p_loss1024, marker='P', label='1024 Bytes')
ax2.plot(p_rate1500, p_loss1500, marker='.', label='1500 Bytes')

ax2.set_title('P4-DPDK',fontsize=fsize+2)
ax2.set_ylim(-5, 100)
ax2.set_xlabel('Rate (Gbps)',fontsize=fsize)
ax2.set_xticks(p_rate1500)
ax2.set_yticklabels([-5,0,20,40,60,80,100],fontsize=fsize-1)
ax2.set_ylabel('Loss (%)',fontsize=fsize)
ax2.grid(True, linestyle='--')

ax1.legend(bbox_to_anchor=(0., 1.1, 2.2, 0.05), loc="upper center", ncol=6, mode="expand", borderaxespad=0.,fontsize=fsize-4,frameon=True)
# plt.savefig('packet_loss.pdf')
# plt.savefig('packet_loss.png')
plt.show()

