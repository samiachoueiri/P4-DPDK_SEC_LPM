import matplotlib.pyplot as plt

# Increase font size globally
# fig = plt.figure(figsize=(14, 10))
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 8))  # 1 row, 2 columns
plt.rcParams.update({'font.size': 24})

s_rate64 = [1, 5, 10]
s_rate128 = [1, 5, 10, 25]
s_rate256 = [1, 5, 10, 25, 50]
s_rate512 = [1, 5, 10, 25, 50, 100]
s_rate1024 = [1, 5, 10, 25, 50, 100]
s_rate1500 = [1, 5, 10, 25, 50, 100]

s_loss64 = [0.05025, 0.6515, 0.8119]
s_loss128 = [0.0081, 0.3452, 0.6772, 0.861]
s_loss256 = [0.001, 0.1344, 0.6147, 0.8259, 0.9246]
s_loss512 = [0.0146, 0.0529, 0.0513, 0.4757, 0.7346, 0.8662]
s_loss1024 = [0.0041, 0.0081, 0.016, 0.006, 0.4065, 0.7167]
s_loss1500 = [0.006, 0, 0, 0.007, 0.2387, 0.626]

p_rate64 = [1, 5, 10]
p_rate128 = [1, 5, 10, 25]
p_rate256 = [1, 5, 10, 25, 50]
p_rate512 = [1, 5, 10, 25, 50, 100]
p_rate1024 = [1, 5, 10, 25, 50, 100]
p_rate1500 = [1, 5, 10, 25, 50, 100]

p_loss64 = [0, 0, 0.2316]
p_loss128 = [0, 0, 0, 0.4315]
p_loss256 = [0, 0, 0, 0, 0.5]
p_loss512 = [0, 0, 0, 0, 0, 0.4985]
p_loss1024 = [0, 0, 0, 0, 0, 0.064]
p_loss1500 = [0, 0, 0, 0, 0, 0.0356]

# Amplify loss values by multiplying by 100
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

# Set bar width
bar_width = 3

ax1.bar(s_rate64, s_loss64, width=bar_width, label='64 Bytes')
ax1.bar(s_rate128, s_loss128, width=bar_width, label='128 Bytes')
ax1.bar(s_rate256, s_loss256, width=bar_width, label='256 Bytes')
ax1.bar(s_rate512, s_loss512, width=bar_width, label='512 Bytes')
ax1.bar(s_rate1024, s_loss1024, width=bar_width, label='1024 Bytes')
ax1.bar(s_rate1500, s_loss1500, width=bar_width, label='1500 Bytes')

ax1.set_title('Suricata DPDK')
ax1.set_ylim(0, 100)
ax1.set_xlabel('Rate (Gbps)')
ax1.set_xticks(s_rate1500)
ax1.set_ylabel('Loss (%)')
ax1.grid(True, linestyle='--')
# ax1.legend(fontsize="16",bbox_to_anchor=(0, 1))

ax2.bar(p_rate64, p_loss64, width=bar_width, label='64 Bytes')
ax2.bar(p_rate128, p_loss128, width=bar_width, label='128 Bytes')
ax2.bar(p_rate256, p_loss256, width=bar_width, label='256 Bytes')
ax2.bar(p_rate512, p_loss512, width=bar_width, label='512 Bytes')
ax2.bar(p_rate1024, p_loss1024, width=bar_width, label='1024 Bytes')
ax2.bar(p_rate1500, p_loss1500, width=bar_width, label='1500 Bytes')

ax2.set_title('P4-DPDK')
ax2.set_ylim(0, 100)
ax2.set_xlabel('Rate (Gbps)')
ax2.set_xticks(p_rate1500)
ax2.set_ylabel('Loss (%)')
ax2.grid(True, linestyle='--')
ax2.legend(fontsize="20")

plt.show()
