import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import pandas as pd
import matplotlib as mpl
from matplotlib.colors import LinearSegmentedColormap

mpl.rcParams['font.size'] = 30

# Core count labels
cores = [1, 2, 3, 4, 5, 6, 7, 8]
core_labels = [str(c) for c in cores]
attack_types = ['TCP \nFlood', 'Heavy \nHitter', 'ICMP \nFlood', 'UDP \nFlood']

# Data for Suricata DPDK
suricata_data = [
    [83.74, 74.41, 64.33, 57.99, 46.14, 43.44, 37.24, 29.46],  # TCP Flood
    [80.98, 71.96, 59.67, 51.04, 47.56, 40.25, 30.34, 28.48],  # Heavy Hitter
    [86.28, 76.08, 65.02, 57.24, 49.70, 41.68, 37.66, 37.12],  # ICMP Flood
    [84.83, 77.33, 67.76, 54.27, 46.24, 41.70, 40.41, 36.12],  # UDP Flood
]

# Data for Proposed System
proposed_data = [
    [74.35, 48.45, 20.21, 0.48, 0.03, 0.03, 0.04, 0.03],       # TCP Flood
    [71.88, 44.44, 15.45, 0.09, 0.01, 0.19, 0.05, 0.02],       # Heavy Hitter
    [73.98, 45.74, 17.15, 1.28, 0.07, 0.06, 0.06, 0.03],       # ICMP Flood
    [75.88, 48.00, 20.89, 2.28, 0.10, 0.46, 0.01, 0.02],       # UDP Flood
]

# Convert to DataFrames
df_suricata = pd.DataFrame(suricata_data, index=attack_types, columns=core_labels)
df_proposed = pd.DataFrame(proposed_data, index=attack_types, columns=core_labels)

# # Plot
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))

# # Set same color range for both heatmaps
# sns.heatmap(df_suricata, annot=True, fmt=".1f", cmap="YlOrRd", cbar=True, ax=ax1, vmin=0, vmax=100)
# ax1.set_title("Suricata DPDK", fontsize=27)
# ax1.set_xlabel("CPU Cores")
# ax1.set_ylabel("Attack Type")

# sns.heatmap(df_proposed, annot=True, fmt=".1f", cmap="YlGn", cbar=True, ax=ax2, vmin=0, vmax=100)
# ax2.set_title("Proposed System", fontsize=27)
# ax2.set_xlabel("CPU Cores")
# ax2.set_ylabel("")

# Custom colormaps
# suricata_cmap = LinearSegmentedColormap.from_list("suricata_cmap", ["#4b8333", "#990000"])
# proposed_cmap = LinearSegmentedColormap.from_list("proposed_cmap", ["#4b8333", "#990000"])

suricata_cmap = LinearSegmentedColormap.from_list("suricata_cmap", ["#6AA84F", "#FFE8A3", "#CB2929"])
proposed_cmap = LinearSegmentedColormap.from_list("proposed_cmap", ["#6AA84F", "#FFE8A3", "#CB2929"])

# Plot
# fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(18, 10))
# Plot
fig = plt.figure(figsize=(18, 10))
gs = fig.add_gridspec(1, 2, width_ratios=[1, 1.25])  # Equal width

ax1 = fig.add_subplot(gs[0])
ax2 = fig.add_subplot(gs[1])

heatmap1 = sns.heatmap(df_suricata, annot=True, fmt=".1f", cmap=proposed_cmap, cbar=False, ax=ax1, vmin=0, vmax=100)
# heatmap1.collections[0].colorbar.ax.tick_params(labelrotation=45)  # Rotate colorbar ticks
for text in heatmap1.texts:
    text.set_rotation(90)
ax1.set_title("Suricata DPDK", fontsize=32)
ax1.set_xlabel("CPU Cores")
# ax1.set_ylabel("Attack Type")

heatmap2 = sns.heatmap(df_proposed, annot=True, fmt=".1f", cmap=proposed_cmap, cbar=True, ax=ax2, vmin=0, vmax=100)
# heatmap2.collections[0].colorbar.ax.tick_params(labelrotation=45)  # Rotate colorbar ticks
for text in heatmap2.texts:
    text.set_rotation(90)
ax2.set_title("Proposed System", fontsize=32)
ax2.set_xlabel("CPU Cores")
ax2.set_ylabel("")
ax2.set_yticklabels([])

plt.tight_layout()
# plt.savefig('loss_cores_hm.pdf')
plt.show()
