import matplotlib.pyplot as plt
import numpy as np

# Define attack types and core counts
attack_labels = ['TCP Flood', 'Heavy Hitter', 'ICMP Flood', 'UDP Flood']
core_counts = [1, 2, 3, 4, 5, 6, 7, 8]
angles = np.linspace(0, 2 * np.pi, len(core_counts), endpoint=False).tolist()
angles += angles[:1]  # Close the loop

# Create function to build radar chart for one system
def plot_radar(ax, title, data_dict):
    for label, values in data_dict.items():
        values += values[:1]  # Close the loop for each attack type
        ax.plot(angles, values, label=label, marker='o')
        ax.fill(angles, values, alpha=0.1)
    
    ax.set_title(title, size=18, y=1.1)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([str(c) for c in core_counts])
    ax.set_yticklabels(['0', '25', '50', '75', '100'])
    ax.set_ylim(0, 100)
    ax.grid(True)
    ax.legend(loc='upper right', bbox_to_anchor=(1.3, 1.1), fontsize=10)

# Data for Suricata DPDK
suricata_data = {
    'TCP Flood': [83.74,74.41,64.33,57.99,46.14,43.44,37.24,29.46],
    'Heavy Hitter': [80.98,71.96,59.67,51.04,47.56,40.25,30.34,28.48],
    'ICMP Flood': [86.28,76.08,65.02,57.24,49.70,41.68,37.66,37.12],
    'UDP Flood': [84.83,77.33,67.76,54.27,46.24,41.70,40.41,36.12],
}

# Data for Proposed System
proposed_data = {
    'TCP Flood': [74.35,48.45,20.21,0.48,0.03,0.03,0.04,0],
    'Heavy Hitter': [71.88,44.44,15.45,0.09,0.01,0.19,0.05,0],
    'ICMP Flood': [73.98,45.74,17.15,1.28,0.07,0.06,0.06,0],
    'UDP Flood': [75.88,48.00,20.89,2.28,0.10,0.46,0.01,0],
}

# Setup plot
fig, (ax1, ax2) = plt.subplots(1, 2, subplot_kw={'polar': True}, figsize=(18, 9))

plot_radar(ax1, "Suricata DPDK", suricata_data)
plot_radar(ax2, "Proposed System", proposed_data)

plt.tight_layout()
plt.show()
