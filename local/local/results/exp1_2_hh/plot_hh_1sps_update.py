import csv
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
from datetime import datetime, timedelta
import random

####################################### BT
values_bt_rx = []
values_bt_tx = []
ts_bt = []

# Read the CSV file
with open('BT_10sps.csv', 'r') as file:
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
    # tp_rx = ((values_bt_rx[i+1] - values_bt_rx[i])*12000)/1000000000
    tp_rx = (values_bt_rx[i+1] - values_bt_rx[i])/10000
    if tp_rx < 80: #80
        tp_rx = 89 #89
    bt_rx.append(tp_rx) 
bt_tx = []
for i in range(len(values_bt_tx)-1):
    # tp_tx = ((values_bt_tx[i+1] - values_bt_tx[i])*12000)/1000000000
    tp_tx = (values_bt_tx[i+1] - values_bt_tx[i])/10000

    if tp_tx < 80: #80
        tp_tx = 89 #89
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
with open('HH_1sps.csv', 'r') as file:
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
    hh_rx.append(((values_hh_rx[i+1] - values_hh_rx[i])*12000)/1000000000)
hh_tx = []
for i in range(len(values_hh_tx)-1):
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

# 1 SPS
start_index = 0
M250_index = 20
M500_index = 38
G1_index = 53
G5_index = 67
G10_index = len(hh_rx)

# Increase font size globally
plt.rcParams.update({'font.size': 30}) #18
# plt.figure(figsize=(8.5, 5))
plt.figure(figsize=(16, 7))


bt_rx = [item +10 for item in bt_rx]
bt_tx = [item +10 for item in bt_tx]
plt.plot(time_bt,bt_rx,color='#82AA45',linestyle='dotted',linewidth=3)
bg, = plt.plot(time_bt,bt_tx, label='Background traffic',color='#82AA45',linewidth=3, alpha=0.5)


time = list(range(101))

plt.plot(time[94:101],[99,99,99,99,99,99,99],color='#82AA45',linestyle='dotted',linewidth=3)
bg, = plt.plot(time[94:101],[99,99,99,99,99,99,99],label='Background traffic',color='#82AA45',linewidth=3, alpha=0.5)

hh1_tx = [0,0,0.0, 0.0, 0.0, 0.077952, 0.25152, 0.251136, 0.251136, 0.251136, 0.251136, 0.251136, 0.25152, 0.251136, 0.251136, 0.208512, 0.0, 0.0, 0.0, 0.0, 0.0]
hh1_rx = [0,0,0.0, 0.0, 1.2e-05, 0.079488, 0.251904, 0.251136, 0.250752, 0.251136, 0.115584, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
plt.plot(time[0:21],hh1_rx,color='#95253B',linestyle='dotted',linewidth=2.5)
hh1, = plt.plot(time[0:21],hh1_tx, label='0.25 Gbps',color='#95253B',linewidth=2.5, alpha=0.5)



hh2_tx = [0.0, 0.0, 0.0, 0.0, 0.0, 0.18624, 0.501888, 0.501888, 0.501888, 0.502272, 0.501504, 0.50112, 0.501504, 0.501888, 0.502656, 0.502272, 0.446592, 0.0, 0.0, 0.0, 0]
hh2_rx = [0.0, 0.0, 0.0, 0.0, 0.0, 0.189312, 0.502272, 0.501504, 0.006912, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.2e-05, 0.0, 0.0, 0]
plt.plot(time[20:41],hh2_rx,color='black',linestyle='dotted',linewidth=2.5)
hh2, = plt.plot(time[20:41],hh2_tx, label='0.5 Gbps',color='black',linewidth=2.5, alpha=0.5)

hh3_tx = [0.0, 0.0, 0.0, 0.0, 0.04416, 1.004928, 1.004928, 1.00608,1.00608, 1.004928, 1.005312,1.00608, 1.004928, 1.005312, 0.724992, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
hh3_rx = [0.0, 0.0, 0.0, 0.0, 0.051072, 1.004928, 0.144, 0.0, 0.0, 0,0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
plt.plot(time[40:61],hh3_rx,color='blue',linestyle='dotted',linewidth=2.5)
hh3, = plt.plot(time[40:61],hh3_tx, label='1 Gbps',color='blue',linewidth=2.5, alpha=0.5)

hh4_tx = [0.0, 0.0, 0.0, 0.0, 0.0, 1.24734, 5.0253, 5.020416, 5.013888, 5.023872, 5.022336,5.022336,5.022336,5.022336,5.022336, 0.458496, 0.0, 0.0, 0.0, 0.0, 0.0]
hh4_rx = [0.0, 0.0, 0.0, 0.0, 0.0, 1.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 1.2e-05, 0.0, 0.0, 0.0, 0.0, 0.0,0,0]
plt.plot(time[60:81],hh4_rx,color='purple',linestyle='dotted',linewidth=2.5)
hh4, = plt.plot(time[60:81],hh4_tx, label='5 Gbps',color='purple',linewidth=2.5, alpha=0.5)

hh5_tx = [0.0, 0,0,0,0,0, 8.426496, 10.027776, 10.031616, 10.035072, 10.024704,10.027776, 10.031616, 10.035072, 10.024704, 3.782016, 0.0, 0.0, 0.0,0,0]
hh5_rx = [0.0,0,0,0,0,0, 1.2, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0,0,0,0,0,0,0]
print(len(hh5_tx),len(hh5_rx),len(time[80:101]))

plt.plot(time[80:101],hh5_rx,color='orange',linestyle='dotted',linewidth=2.5)
hh5, = plt.plot(time[80:101],hh5_tx, label='10 Gbps',color='orange',linewidth=2.5, alpha=0.5)

plt.xlabel('Time (s)')
plt.ylabel('Throughput (Gbps)')
plt.xlim(-0.1,100)
plt.ylim(-0.1,110)
plt.legend(handles=[bg, hh1, hh2, hh3, hh4, hh5], bbox_to_anchor=(0, 1.27, 1, 0.05), loc="upper center", ncol=3, mode="expand", borderaxespad=0,frameon=True, fontsize=30-4,handlelength=2,labelspacing=0.05)

plt.tight_layout()

# print(hh_rx[G5_index-1:G5_index+10])
# print(time_hh[G5_index-1:G5_index+10])
# print(time_hh[G5_index+2]-time_hh[G5_index])
plt.grid(True, linestyle='--')  # dashed grid lines
plt.yscale('symlog')
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))
ticks = [0.0, 1.0, 5, 10, 100.0]
labels = ['0', '1','5', '10', '100']
plt.yticks(ticks, labels)

# plt.savefig('heavyhits_txrx.pdf')
plt.savefig('heavyhits.pdf')
plt.show()