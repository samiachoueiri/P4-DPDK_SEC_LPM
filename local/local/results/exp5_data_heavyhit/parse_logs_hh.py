import re
import matplotlib.pyplot as plt
from matplotlib.ticker import ScalarFormatter
import numpy as np
import csv

def extract_log(log_file):
    with open(log_file, 'r') as file:
        log_content = file.read()

    outgoing_values = re.findall(r'Outgoing:.*?Curr: ([0-9.]+) MBit/s', log_content)
    incoming_values = re.findall(r'Incoming:.*?Curr: ([0-9.]+) MBit/s', log_content)

    return outgoing_values, incoming_values

def extract_hh(hh_file):
    values_hh_rx = []
    values_hh_tx = []
    # Read data from CSV file
    with open(hh_file, 'r') as file:
        csv_reader = csv.reader(file)
        next(csv_reader)  # Skip header row
        for row in csv_reader:
            values_hh_rx.append(float(row[0]))
            values_hh_tx.append(float(row[1]))

    hh_rx = []
    for i in range(len(values_hh_rx)-1):
        hh_rx.append((values_hh_rx[i+1] - values_hh_rx[i])/10) 
    hh_tx = []
    for i in range(len(values_hh_tx)-1):
        hh_tx.append((values_hh_tx[i+1] - values_hh_tx[i])/10)
    
    return hh_rx, hh_tx

def plot_values(time,hh_rx_values,hh_tx_values,outgoing_values, incoming_values,clr):
    # plt.plot(outgoing_values, label='MAWI trace TX',color='#82AA45',linewidth=5,linestyle='dotted')
    # plt.plot(incoming_values, label='MAWI trace RX',color='#82AA45',linewidth=5, alpha=0.2)
    # plt.plot(time+15,hh_tx_values, label='Heavy hitter TX',color='#95253B',linestyle='dotted',linewidth=5)
    # plt.plot(time+15,hh_rx_values, label='Heavy hitter RX',color='#95253B',linewidth=5)
    plt.plot(outgoing_values, label='MAWI trace TX',color=clr,linestyle='dotted',linewidth=5)
    plt.plot(incoming_values, label='MAWI trace RX',color=clr,linewidth=5, alpha=0.2)
    plt.plot(time+15,hh_tx_values, label='Heavy hitter TX',color='#95253B',linestyle='dotted',linewidth=5)
    plt.plot(time+15,hh_rx_values, label='Heavy hitter RX',color='#95253B',linewidth=5)
    plt.xlabel('Time (s)')
    plt.ylabel('Throughput (Mbps)')
    plt.xlim(0,30)
    plt.ylim(0,1100)
    plt.grid(True, linestyle='--')  # dashed grid lines

# Initialize lists to store data
packet_sizes = []
jan_count = []
feb_count = []
mar_count = []
apr_count = []

# Read data from CSV file
with open('pcap_pkt_distribution.csv', 'r') as file:
    csv_reader = csv.reader(file)
    next(csv_reader)  # Skip header row
    for row in csv_reader:
        packet_sizes.append(int(row[0]))
        jan_count.append(float(row[1]))
        feb_count.append(float(row[2]))
        mar_count.append(float(row[3]))
        apr_count.append(float(row[4]))



plt.rcParams.update({'font.size': 22})
plt.figure(figsize=(14, 18))
plt.subplot(5, 1, 1)
plt.plot(packet_sizes, jan_count, label='Dataset 1',color='seagreen')
plt.plot(packet_sizes, feb_count, label='Dataset 2',color='gold')
plt.plot(packet_sizes, mar_count, label='Dataset 3',color='mediumpurple')
plt.plot(packet_sizes, apr_count, label='Dataset 4',color='cornflowerblue')
plt.xlabel('Packet Size (Bytes)')
plt.ylabel('CDF')
plt.grid(True)
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc="lower center", ncol=4, mode="expand", borderaxespad=0.,fontsize=18)
#--------------------------- JAN --------------
hh_file = 'Jan_hh.csv'
hh_rx, hh_tx = extract_hh(hh_file)
time = np.arange(0, len(hh_tx) / 10, 0.1)
hh_rx_values = [float(x) for x in hh_rx]
hh_tx_values = [float(x) for x in hh_tx]
log_file = "jan.log"
outgoing, incoming = extract_log(log_file)
outgoing_values = [float(x) for x in outgoing]
incoming_values = [float(x) for x in incoming]
plt.subplot(5, 1, 2)
#plt.title('January 27, 2024')
plot_values(time,hh_rx_values,hh_tx_values,outgoing_values, incoming_values,'gold')
plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc="lower center", ncol=4, mode="expand", borderaxespad=0.,fontsize=18)
#--------------------------- FEB --------------
hh_file = 'Feb_hh.csv'
hh_rx, hh_tx = extract_hh(hh_file)
time = np.arange(0, len(hh_tx) / 10, 0.1)
hh_rx_values = [float(x) for x in hh_rx]
hh_tx_values = [float(x) for x in hh_tx]
log_file = "feb.log"
outgoing, incoming = extract_log(log_file)
outgoing_values = [float(x) for x in outgoing]
incoming_values = [float(x) for x in incoming]
plt.subplot(5, 1, 3)
#plt.title('February 10, 2024')
plot_values(time,hh_rx_values,hh_tx_values,outgoing_values, incoming_values,'gold')
# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc="lower center", ncol=4, mode="expand", borderaxespad=0.,fontsize=18)
#--------------------------- MAR --------------
hh_file = 'Mar_hh.csv'
hh_rx, hh_tx = extract_hh(hh_file)
time = np.arange(0, len(hh_tx) / 10, 0.1)
hh_rx_values = [float(x) for x in hh_rx]
hh_tx_values = [float(x) for x in hh_tx]
log_file = "mar.log"
outgoing, incoming = extract_log(log_file)
outgoing_values = [float(x) for x in outgoing]
incoming_values = [float(x) for x in incoming]
plt.subplot(5, 1, 4)
#plt.title('March 23, 2024')
plot_values(time,hh_rx_values,hh_tx_values,outgoing_values, incoming_values,'mediumpurple')
# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc="lower center", ncol=4, mode="expand", borderaxespad=0.,fontsize=18)
#--------------------------- APR --------------
hh_file = 'Apr_hh.csv'
hh_rx, hh_tx = extract_hh(hh_file)
time = np.arange(0, len(hh_tx) / 10, 0.1)
hh_rx_values = [float(x) for x in hh_rx]
hh_tx_values = [float(x) for x in hh_tx]
log_file = "apr.log"
outgoing, incoming = extract_log(log_file)
outgoing_values = [float(x) for x in outgoing]
incoming_values = [float(x) for x in incoming]
plt.subplot(5, 1, 5)
#plt.title('April 07, 2024')
plot_values(time,hh_rx_values,hh_tx_values,outgoing_values, incoming_values,'cornflowerblue')
# plt.legend(bbox_to_anchor=(0., 1.02, 1., .102), loc="lower center", ncol=4, mode="expand", borderaxespad=0.,fontsize=18)
#plt.legend(loc="lower left",fontsize=11)
plt.tight_layout()
# plt.savefig("logs_hh_data_3.pdf")
# plt.savefig("test.pdf")
# plt.savefig("logs_hh.png")
plt.show()

