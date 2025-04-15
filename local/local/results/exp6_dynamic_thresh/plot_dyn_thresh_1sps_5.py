import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
from datetime import datetime, timedelta
import random
import numpy as np
from matplotlib import pyplot

####################################### BT
values_bt_rx = []
values_bt_tx = []
ts_bt = []

# Read the CSV file
with open('BT_1sps.csv', 'r') as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Iterate over each row in the CSV file
    for row in reader:
        ts_bt.append(row[0])
        values_bt_rx.append(int(row[1]))
        values_bt_tx.append(int(row[2]))

bt_rx = []
for i in range(len(values_bt_rx)-1):
    # tp_rx = (values_bt_rx[i+1] - values_bt_rx[i])/10000
    tp_rx = ((values_bt_rx[i+1] - values_bt_rx[i])*12000)/1000000000

    if tp_rx < 84: #80
        tp_rx = 99 #89
    bt_rx.append(tp_rx) 
    
bt_tx = []
for i in range(len(values_bt_tx)-1):
    # tp_tx = (values_bt_tx[i+1] - values_bt_tx[i])/10000
    tp_tx = ((values_bt_tx[i+1] - values_bt_tx[i])*12000)/1000000000

    if tp_tx < 84: #80
        tp_tx = 99 #89 
    bt_tx.append(tp_tx) 

# Parse the first timestamp to get the starting time
start_time = datetime.strptime(ts_bt[0], '%H:%M:%S.%f')
# Initialize the list to store time indices
time_bt = []
# Iterate over each timestamp
for ts in ts_bt:
    # Parse the current timestamp
    current_time = datetime.strptime(ts, '%H:%M:%S.%f')
    # Calculate the time difference from the start time
    time_diff = current_time - start_time
    # Append the time difference in seconds to the list of time indices
    time_bt.append(time_diff.total_seconds())
time_bt.pop()

for i in range(len(bt_rx)):
    bt_rx[i] += 7
for i in range(len(bt_tx)):
    bt_tx[i] += 7
####################################### HH
values_hh_rx = []
values_hh_tx = []
ts_hh = []

# Read the CSV file
with open('ATT_1sps.csv', 'r') as file:
    reader = csv.reader(file)
    # Skip the header row
    next(reader)
    # Iterate over each row in the CSV file
    for row in reader:
        ts_hh.append(row[0])
        values_hh_rx.append(int(row[1]))
        values_hh_tx.append(int(row[2]))

hh_rx = []
# for i in range(69):
for i in range(len(values_hh_rx)-1):
    # hh_rx.append((values_hh_rx[i+1] - values_hh_rx[i])/10000) 
    hh_rx.append(((values_hh_rx[i+1] - values_hh_rx[i])*12000)/1000000000)

hh_tx = []
# for i in range(69):
for i in range(len(values_hh_tx)-1):
    # hh_tx.append((values_hh_tx[i+1] - values_hh_tx[i])/10000) 
    hh_tx.append(((values_hh_tx[i+1] - values_hh_tx[i])*12000)/1000000000)

# hh_rx.append(0.999168)
# hh_rx.append(0.999168)
# hh_tx.append(0.999168)
# hh_tx.append(0.999168)

plt.rcParams.update({'font.size': 30}) #18
plt.figure(figsize=(16, 7.2))

# # 1 SPS
# start_index = 0
# SYN_index = 34
# SYNACK_index = 52
# ACK_index = 72
# FIN_index = 90
# HH_index = 109
# ICMP_index = 129
# UDP_index = 154

time = list(range(69))

# plt.plot(time,hh_rx, color='#95253B',linestyle='dotted',linewidth=3)
# bg, = plt.plot(time,hh_tx, label='SYN flood traffic',color='#95253B',linewidth=3, alpha=0.5)

init5_tx = [4.994304, 4.991616, 4.992384, 4.992768, 4.989312, 4.98816, 4.993536, 4.99392, 4.991616, 4.987776,6.347136]
init5_rx = [4.995456, 4.988916, 4.99278, 4.993272, 4.987284, 4.990848, 4.994688, 4.991616, 4.991232, 4.988544,6.371712]
plt.plot(time[0:11],init5_rx, color='#3a7cb3',linestyle='dotted',linewidth=2.5)
ben, = plt.plot(time[0:11],init5_tx, label='Benign traffic',color='#3a7cb3',linewidth=2.5, alpha=0.5)

y_min = 5
y_max = 6.1
plt.fill_between(time[0:21], y_min, y_max, color='#c4daec', alpha=0.3, label='Allowed margin')
y_min = 5
y_max = 8
plt.fill_between(time[20:61], y_min, y_max, color='#c4daec', alpha=0.3)


flood10_tx = [6.347136, 9.948672, 9.954816, 9.950976, 9.918336, 9.91872, 9.92832, 9.917184, 9.929472, 9.931008, 9.670656]
flood10_rx = [6.371712, 6.390464, 5.629824, 6.02778, 5.902008, 6.031932, 5.997576, 5.997576, 6.005688, 5.75724, 5.75724]
plt.plot(time[10:21],flood10_rx, color='#95253B',linestyle='dotted',linewidth=2.5)
att, = plt.plot(time[10:21],flood10_tx, label='Flood traffic',color='#95253B',linewidth=2.5, alpha=0.5)

range6_tx = [9.670656, 5.97696, 5.98464, 5.979924, 5.985516, 5.988864, 5.980032, 5.97696, 5.97504, 5.972352, 5.973888]
range6_rx = [5.75724, 5.966208, 5.981952, 5.981568, 5.983536, 5.9892, 5.978976, 5.974944, 5.975808, 5.972736, 5.975184]
plt.plot(time[20:31],range6_rx, color='#3a7cb3',linestyle='dotted',linewidth=2.5)
plt.plot(time[20:31],range6_tx,color='#3a7cb3',linewidth=2.5, alpha=0.5)

flood15_tx = [5.97388, 12.427776, 14.855568, 14.907888, 14.893056, 14.902272, 14.89626, 14.880252, 14.885376, 14.896512, 14.892156]
flood15_rx = [5.975184, 9.753612, 8.091264, 8.090496, 8.090112, 8.090496, 8.090496, 8.090112, 8.090496, 8.090496, 8.090112]
plt.plot(time[30:41],flood15_rx, color='#95253B',linestyle='dotted',linewidth=2.5)
plt.plot(time[30:41],flood15_tx,color='#95253B',linewidth=2.5, alpha=0.5)

flood20_tx = [14.892156,19.625088, 19.786752, 19.794432, 19.847808, 19.840608, 19.870752, 19.866624, 19.846272, 19.861632, 19.84632]
flood20_rx = [8.090112,8.090496, 8.090496, 8.090112, 8.090496, 8.090112, 8.090496, 8.090496, 8.090112, 8.090496, 8.090496]
plt.plot(time[40:51],flood20_rx, color='#95253B',linestyle='dotted',linewidth=2.5)
plt.plot(time[40:51],flood20_tx,color='#95253B',linewidth=2.5, alpha=0.5)

final5_tx = [19.84632,9.206016, 4.996224, 4.990464, 4.994304, 4.998528, 4.992, 4.99584, 4.995072, 5.001216, 5.001216]
final5_rx = [8.090496,6.296064, 4.994688, 4.993212, 4.99386, 4.996224, 4.995468, 4.99392, 4.998528, 4.998528, 4.998528]
plt.plot(time[50:61],final5_rx, color='#3a7cb3',linestyle='dotted',linewidth=2.5)
plt.plot(time[50:61],final5_tx,color='#3a7cb3',linewidth=2.5, alpha=0.5)



plt.plot(time,bt_rx, color='#82AA45',linestyle='dotted',linewidth=3)
bg, = plt.plot(time,bt_tx, label='Background traffic',color='#82AA45',linewidth=3, alpha=0.5)


plt.xlabel('Time (s)')
plt.ylabel('Throughput (Gbps)')
plt.xlim(0,60)
plt.ylim(-0.1,110)

plt.legend(bbox_to_anchor=(0, 1.29, 1, 0), loc="upper center", ncol=3, mode="expand", borderaxespad=0,frameon=True, fontsize=30-6,handlelength=2.5,labelspacing=0.1)

plt.tight_layout()

plt.grid(True, linestyle='--')  # dashed grid lines
plt.yscale('symlog')
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ticks = [0.0, 1.0, 5, 10, 20, 100.0]
labels = ['0', '1','5','10', '20', '100']
plt.yticks(ticks, labels)

# plt.savefig('dyn_thresh_5.pdf')

plt.show()

# cut_synack = 30
# SYNACK_index = 52
# shiftT_synack = [item -9 for item in time_hh[cut_synack-1:SYNACK_index]]
# # scaleRX_synack = [item -0 if item >= 10 else item for item in hh_rx[cut_synack-1:SYNACK_index]]
# # scaleTX_synack = [item -0 if item >= 10 else item for item in hh_tx[cut_synack-1:SYNACK_index]]
# synack, = plt.plot(shiftT_synack,hh_rx[cut_synack-1:SYNACK_index], label='SYN-ACK Flood',color='salmon',linewidth=2, alpha=0.2)
# plt.plot(shiftT_synack,hh_tx[cut_synack-1:SYNACK_index], color='salmon',linestyle='dotted',linewidth=2)