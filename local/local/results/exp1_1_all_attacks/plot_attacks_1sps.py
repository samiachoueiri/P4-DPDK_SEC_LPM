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
for i in range(len(values_hh_rx)-1):
    # hh_rx.append((values_hh_rx[i+1] - values_hh_rx[i])/10000) 
    hh_rx.append(((values_hh_rx[i+1] - values_hh_rx[i])*12000)/1000000000)

hh_tx = []
for i in range(len(values_hh_tx)-1):
    # hh_tx.append((values_hh_tx[i+1] - values_hh_tx[i])/10000) 
    hh_tx.append(((values_hh_tx[i+1] - values_hh_tx[i])*12000)/1000000000)

# Parse the first timestamp to get the starting time
start_time = datetime.strptime(ts_hh[0], '%H:%M:%S.%f')
# Initialize the list to store time indices
time_hh = []
# Iterate over each timestamp
for ts in ts_hh:
    # Parse the current timestamp
    current_time = datetime.strptime(ts, '%H:%M:%S.%f')
    # Calculate the time difference from the start time
    time_diff = current_time - start_time
    # Append the time difference in seconds to the list of time indices
    time_hh.append(time_diff.total_seconds())
time_hh.pop()

time = list(range(141))

plt.rcParams.update({'font.size': 30}) #18
plt.figure(figsize=(16, 7.2))

# 1 SPS
start_index = 0
SYN_index = 34
SYNACK_index = 52
ACK_index = 72
FIN_index = 90
HH_index = 109
ICMP_index = 129
UDP_index = 154

time_bt = list(range(153))
plt.plot(time_bt,bt_rx, color='#82AA45',linestyle='dotted',linewidth=3)
bg, = plt.plot(time_bt,bt_tx, label='Background traffic',color='#82AA45',linewidth=3, alpha=0.5)



syn_tx = [0,0.0, 0.0, 0.0, 0.0, 0.0, 19.687884, 19.779012, 19.786224, 19.808136, 19.809012, 19.801092, 19.801344, 19.804416, 19.805568, 15.239808, 0.0, 0.0, 0.0, 0.0, 0.0]
syn_rx = [0,0.0, 0.0, 0.0, 0.0, 0.0, 19.759116, 19.777908, 16.98432, 14.905728, 14.904192, 14.899656, 14.898756, 14.901144, 14.904168, 11.415552, 1.2e-05, 0.0, 0.0, 0.0, 0.0]
plt.plot(time_bt[0:21],syn_rx, color='#95253B',linestyle='dotted',linewidth=2.5)
syn, = plt.plot(time_bt[0:21],syn_tx, label='SYN Flood',color='#95253B',linewidth=2.5, alpha=0.5)


synack_tx = [0,0.0, 0.0, 0.0, 0.0, 14.565924, 19.791708, 19.811712, 19.840128, 19.848576, 19.841664,19.841664,19.841664, 19.836708, 8.931036, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
synack_rx = [0,0.0, 0.0, 0.0, 0.0, 14.653056, 19.77642, 16.723224, 10.020036, 10.020072, 10.019676, 10.019676,10.019676, 10.0167, 4.471296, 0.0, 1.2e-05, 0.0, 0.0, 0.0, 0.0]
plt.plot(time_bt[20:41],synack_rx, color='salmon',linestyle='dotted',linewidth=2.5)
synack, = plt.plot(time_bt[20:41],synack_tx, label='SYN-ACK Flood',color='salmon',linewidth=2.5, alpha=0.5)

ack_tx = [0.0, 0.0, 0.0, 0.0, 0.0, 6.633396, 19.80654, 19.859328, 19.858944, 19.86432, 19.86048,19.86048,19.86048, 19.850112, 19.84512, 2.105088, 0.0, 0.0, 0.0, 0.0, 0.0]
ack_rx = [0.0, 0.0, 0.0, 0.0, 0.0, 6.71424, 19.806288, 19.838256, 6.336768, 5.11296, 5.109888,5.109888,5.109888, 5.109504, 5.10912, 0.523776, 0.0, 0.0, 0.0, 0.0, 0.0]
plt.plot(time_bt[40:61],ack_rx, color='blue',linestyle='dotted',linewidth=2.5)
ack, = plt.plot(time_bt[40:61],ack_tx, label='ACK Flood',color='blue',linewidth=2.5, alpha=0.25)

fin_tx = [0,0,0.0, 0.0, 0.0, 2.806272, 19.866624, 19.868544, 19.868172, 19.871016,19.871016,19.871016,19.871016,19.871016,19.871016, 7.766604, 0.0, 0.0, 0.0, 0.0, 0.0]
fin_rx = [0,0,0.0, 0.0, 0.0, 0.0, 1.2e-05, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
plt.plot(time_bt[60:81],fin_rx, color='magenta',linestyle='dotted',linewidth=2.5)
fin, = plt.plot(time_bt[60:81],fin_tx, label='FIN Flood',color='magenta',linewidth=2.5, alpha=0.5)

# hh__tx = [0.0, 0.0, 0.0, 0.0, 0.0, 0.069888, 9.943392, 9.954336, 9.955968, 9.952896,9.952896,9.952896,9.952896, 9.951744, 1.087872, 0.0, 0.0, 0.0, 0.0, 0.0,0]
hh__tx = [0.0, 0.0, 0.0, 0.0, 0.0, 0.069888, 19.943392, 19.954336, 19.955968, 19.952896,19.952896,19.952896,19.952896, 19.951744, 1.087872, 0.0, 0.0, 0.0, 0.0, 0.0,0]
hh__rx = [0.0, 0.0, 0.0, 0.0, 0.0, 0.106476, 1.093524, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.2e-05, 0.0, 0.0,0]
plt.plot(time_bt[80:101],hh__rx, color='brown',linestyle='dotted',linewidth=2.5)
hh, = plt.plot(time_bt[80:101],hh__tx, label='Heavy Hitter',color='brown',linewidth=2.5, alpha=0.5)

icmp_tx = [0.0, 0.0, 0.0, 0.0, 0.0, 19.33504, 19.949056, 19.963264, 19.955584, 19.95904, 19.952128,19.952128,19.952128,19.952128, 13.801216, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
icmp_rx = [0.0, 0.0, 0.0, 0.0, 0.0, 2.4, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
plt.plot(time_bt[100:121],icmp_rx, color='purple',linestyle='dotted',linewidth=2.5)
icmp, = plt.plot(time_bt[100:121],icmp_tx, label='ICMP Flood',color='purple',linewidth=2.5, alpha=0.5)



udp_tx = [0.0, 0.0, 0.0, 0.0, 0.0, 9.4509, 19.82142, 19.817856, 19.863936, 19.84578, 19.871724, 19.870464, 19.866456, 19.845672, 9.151104, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]   
udp_rx = [0.0, 0.0, 0.0, 0.0, 0.0, 9.537024, 19.821324, 18.622452, 10.640268, 10.027008, 10.035864, 10.027416, 10.02888, 10.022784, 4.579968, 0.0, 0.0, 0.0, 0.0, 0.0,0]
plt.plot(time_bt[120:141],udp_rx, color='orange',linestyle='dotted',linewidth=2.5)
udp, = plt.plot(time_bt[120:141],udp_tx, label='UDP Flood',color='orange',linewidth=2.5, alpha=0.5)


plt.xlabel('Time (s)')
plt.ylabel('Throughput (Gbps)')
plt.xlim(0,140)
plt.ylim(-0.1,110)
attacks = [bg, syn, synack, ack, fin, hh, icmp, udp]
plt.legend(handles=[bg, syn, synack, ack, fin, hh, icmp, udp], bbox_to_anchor=(0, 1.29, 1, 0), loc="upper center", ncol=4, mode="expand", borderaxespad=0,frameon=True, fontsize=30-6,handlelength=1,labelspacing=0.1)

plt.tight_layout()

plt.grid(True, linestyle='--')  # dashed grid lines
plt.yscale('symlog')
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ticks = [0.0, 1.0, 5, 10, 20, 100.0]
labels = ['0', '1','2.5','5', '10', '100']
plt.yticks(ticks, labels)

# plt.savefig('attacks.pdf')

plt.show()

# cut_synack = 30
# SYNACK_index = 52
# shiftT_synack = [item -9 for item in time_hh[cut_synack-1:SYNACK_index]]
# # scaleRX_synack = [item -0 if item >= 10 else item for item in hh_rx[cut_synack-1:SYNACK_index]]
# # scaleTX_synack = [item -0 if item >= 10 else item for item in hh_tx[cut_synack-1:SYNACK_index]]
# synack, = plt.plot(shiftT_synack,hh_rx[cut_synack-1:SYNACK_index], label='SYN-ACK Flood',color='salmon',linewidth=2, alpha=0.2)
# plt.plot(shiftT_synack,hh_tx[cut_synack-1:SYNACK_index], color='salmon',linestyle='dotted',linewidth=2)