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

# no delay
# start_index = 0
# SYN_index = 4181
# SYNACK_index = 7789
# ACK_index = 11277
# FIN_index = 14077
# HH_index = 16792
# ICMP_index = 19917
# UDP_index = 22801

# # 10 SPS
# start_index = 0
# M250_index = 272
# M500_index = 444
# G1_index = 611
# G5_index = 760
# G10_index = 879

# 1 SPS
start_index = 0
M250_index = 20
M500_index = 38
G1_index = 53
G5_index = 67
G10_index = len(hh_rx)

# Increase font size globally
plt.rcParams.update({'font.size': 18}) #18
# plt.figure(figsize=(8.5, 5))
plt.figure(figsize=(9, 6))

plt.plot(time_bt,bt_rx, label='Background traffic RX',color='#82AA45',linewidth=2, alpha=0.2)
plt.plot(time_bt,bt_tx, label='Background traffic TX',color='#82AA45',linestyle='dotted',linewidth=2)
plt.plot(time_hh[start_index:M250_index],hh_rx[start_index:M250_index], label='Heavy Hitter 250 Mbps RX',color='#95253B',linewidth=2, alpha=0.2)
plt.plot(time_hh[start_index:M250_index],hh_tx[start_index:M250_index], label='Heavy Hitter 250 Mbps TX',color='#95253B',linestyle='dotted',linewidth=2)
plt.plot(time_hh[M250_index-1:M500_index],hh_rx[M250_index-1:M500_index], label='Heavy Hitter 500 Mbps RX',color='black',linewidth=2, alpha=0.2)
plt.plot(time_hh[M250_index-1:M500_index],hh_tx[M250_index-1:M500_index], label='Heavy Hitter 500 Mbps TX',color='black',linestyle='dotted',linewidth=2)
plt.plot(time_hh[M500_index-1:G1_index],hh_rx[M500_index-1:G1_index], label='Heavy Hitter 1 Gbps RX',color='blue',linewidth=2, alpha=0.2)
plt.plot(time_hh[M500_index-1:G1_index],hh_tx[M500_index-1:G1_index], label='Heavy Hitter 1 Gbps TX',color='blue',linestyle='dotted',linewidth=2)
plt.plot(time_hh[G1_index-1:G5_index],hh_rx[G1_index-1:G5_index], label='Heavy Hitter 5 Gbps RX',color='purple',linewidth=2, alpha=0.2)
plt.plot(time_hh[G1_index-1:G5_index],hh_tx[G1_index-1:G5_index], label='Heavy Hitter 5 Gbps TX',color='purple',linestyle='dotted',linewidth=2)
plt.plot(time_hh[G5_index-1:G10_index],hh_rx[G5_index-1:G10_index], label='Heavy Hitter 10 Gbps RX',color='orange',linewidth=2, alpha=0.2)
plt.plot(time_hh[G5_index-1:G10_index],hh_tx[G5_index-1:G10_index], label='Heavy Hitter 10 Gbps TX',color='orange',linestyle='dotted',linewidth=2)

plt.xlabel('Time (s)')
plt.ylabel('Throughput (Gbps)')
plt.xlim(0,min([time_bt[-1],time_hh[-1]]))
plt.ylim(-0.1,110)
# plt.legend(bbox_to_anchor=(0., 1.1005, 1, 0.05), loc="upper center", ncol=4, mode="expand", borderaxespad=0.,frameon=True, fontsize=10)
plt.legend(bbox_to_anchor=(0, 1.3, 1, 0), loc="upper center", ncol=3, mode="expand", borderaxespad=0,frameon=True, fontsize=11.25,labelspacing=0.5)

plt.tight_layout()

# print(hh_rx[G5_index-1:G5_index+10])
# print(time_hh[G5_index-1:G5_index+10])
# print(time_hh[G5_index+2]-time_hh[G5_index])
plt.grid(True, linestyle='--')  # dashed grid lines
plt.yscale('symlog')
plt.gca().yaxis.set_major_formatter(ScalarFormatter(useMathText=True))

# plt.savefig('heavyhits1.pdf')
# plt.savefig('heavyhits.png')
plt.show()