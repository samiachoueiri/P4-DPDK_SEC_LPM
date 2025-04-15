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

plt.rcParams.update({'font.size': 32}) #18
plt.figure(figsize=(16, 8))

# # 1 SPS
# start_index = 0
# SYN_index = 34
# SYNACK_index = 52
# ACK_index = 72
# FIN_index = 90
# HH_index = 109
# ICMP_index = 129
# UDP_index = 154

# print(hh_tx)
# print(hh_rx)

# time = list(range(69))
time = list(range(len(hh_rx)))
# plt.plot(time,hh_rx, color='#95253B',linestyle='dotted',linewidth=3)
# bg, = plt.plot(time,hh_tx, label='SYN flood traffic',color='#95253B',linewidth=3, alpha=0.5)

init1_tx = [0.998784, 0.999168, 0.9984, 0.998784, 0.9984, 0.9984, 0.9984, 0.9984, 0.998784, 0.9984, 0.998016]
init1_rx = [0.999168, 0.998784, 0.9984, 0.9984, 0.9984, 0.9984, 0.998784, 0.9984, 0.998784, 0.998016, 0.998016]
plt.plot(time[0:11],init1_rx, color='#3a7cb3',linestyle='dotted',linewidth=3)
ben, = plt.plot(time[0:11],init1_tx, label='Benign traffic',color='#3a7cb3',linewidth=3, alpha=0.8)

y_min = 1
y_max = 1.25
plt.fill_between(time[0:21], y_min, y_max, color='#c4daec', alpha=0.5, label='Allowed margin')
y_min = 1
y_max = 1.5
plt.fill_between(time[20:61], y_min, y_max, color='#c4daec', alpha=0.5)


flood5_tx = [0.9984, 4.131072, 4.988544, 4.987776, 4.986624, 4.987392, 4.988544, 4.992, 4.995072, 4.992, 4.990848]
flood5_rx = [0.9984, 1.817856, 1.184256, 1.184268, 1.184256, 1.184256, 1.184256, 1.184256, 1.184256, 1.184256, 1.184256]
plt.plot(time[10:21],flood5_rx, color='#95253B',linestyle='dotted',linewidth=3)
att, = plt.plot(time[10:21],flood5_tx, label='Flood traffic',color='#95253B',linewidth=3, alpha=0.8)

range1_2_tx = [4.990464, 1.35168, 1.199616, 1.199232, 1.2, 1.199232, 1.199616, 1.199232, 1.199616, 1.199616, 1.2]
range1_2_rx = [1.184256, 0.938432, 1.132032, 1.19808, 1.2, 1.199232, 1.199232, 1.199232, 1.200384, 1.199232, 1.2]
plt.plot(time[20:31],range1_2_rx, color='#3a7cb3',linestyle='dotted',linewidth=3)
plt.plot(time[20:31],range1_2_tx,color='#3a7cb3',linewidth=3, alpha=0.8)

flood10_tx = [1.2, 3.403776, 9.975552, 9.982848, 9.98058, 9.983196, 9.97632, 9.985152, 9.980928, 9.972864, 9.981696]
flood10_rx = [1.199616, 1.784064, 1.442688, 1.442304, 1.442304, 1.442316, 1.442316, 1.442304, 1.442304, 1.442304, 1.442304]
plt.plot(time[30:41],flood10_rx, color='#95253B',linestyle='dotted',linewidth=3)
plt.plot(time[30:41],flood10_tx,color='#95253B',linewidth=3, alpha=0.8)

flood20_tx = [9.972096, 17.44704, 19.871232, 19.882728, 19.888536, 19.896192, 19.891572, 19.87284, 19.85598, 19.877208, 19.883808]
flood20_rx = [1.442304, 1.442304, 1.442304, 1.442304, 1.442304, 1.442304, 1.442304, 1.442304, 1.442304, 1.442304, 1.442304]
plt.plot(time[40:51],flood20_rx, color='#95253B',linestyle='dotted',linewidth=3)
plt.plot(time[40:51],flood20_tx,color='#95253B',linewidth=3, alpha=0.8)

final1_tx = [19.869888, 8.720064, 0.999168, 0.998784, 1.001088, 0.999168, 0.999552, 0.999552, 1.000704, 0.999168, 0.999168]
final1_rx = [1.442304, 1.442304, 0.916224, 1.00032, 0.999936, 0.999168, 0.999552, 0.999936, 0.999552, 0.999948, 0.999168]
plt.plot(time[50:61],final1_rx, color='#3a7cb3',linestyle='dotted',linewidth=3)
plt.plot(time[50:61],final1_tx,color='#3a7cb3',linewidth=3, alpha=0.8)


time = list(range(len(bt_rx)))
plt.plot(time,bt_rx, color='#82AA45',linestyle='dotted',linewidth=3)
bg, = plt.plot(time,bt_tx, label='Background traffic',color='#82AA45',linewidth=3, alpha=0.8)


plt.xlabel('Time (s)')
plt.ylabel('Throughput (Gbps)')
plt.xlim(0,60)
plt.ylim(-0.1,110)

plt.legend(bbox_to_anchor=(0, 1.29, 1, 0), loc="upper center", ncol=3, mode="expand", borderaxespad=0,frameon=True, fontsize=30,handlelength=1.5,labelspacing=0.1)

plt.tight_layout()

plt.grid(True, linestyle='--')  # dashed grid lines
plt.yscale('symlog')
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ticks = [0.0, 1.0, 5, 10, 20, 100.0]
labels = ['0', '1','5','10', '20', '100']
plt.yticks(ticks, labels)

# plt.savefig('dyn_thresh_1.pdf')

plt.show()

# cut_synack = 30
# SYNACK_index = 52
# shiftT_synack = [item -9 for item in time_hh[cut_synack-1:SYNACK_index]]
# # scaleRX_synack = [item -0 if item >= 10 else item for item in hh_rx[cut_synack-1:SYNACK_index]]
# # scaleTX_synack = [item -0 if item >= 10 else item for item in hh_tx[cut_synack-1:SYNACK_index]]
# synack, = plt.plot(shiftT_synack,hh_rx[cut_synack-1:SYNACK_index], label='SYN-ACK Flood',color='salmon',linewidth=2, alpha=0.2)
# plt.plot(shiftT_synack,hh_tx[cut_synack-1:SYNACK_index], color='salmon',linestyle='dotted',linewidth=2)