import numpy as np
import matplotlib.pyplot as plt
import matplotlib as mpl

# Increase font size globally
fsize = 37
mpl.rcParams['font.size'] = fsize

# Load and process data1
data1 = np.loadtxt("out.txt")

def process_data(data):
    time = data[:, 0]
    actual = data[:, 3] / 1000
    predicted = data[:, 4] / 1000
    allowed = data[:, 5] / 1000
    return (
        time[:-1],
        actual[:-1],
        predicted[1:],
        allowed[1:]
    )

time1, actual1, predicted1, allowed1 = process_data(data1)
# time1 -= 6  # Apply time shift
time1 = list(range(len(actual1)))
time1 = [i / 3600 for i in range(len(actual1))]
xticks = range(0, int(time1[-1]) + 1, 1)

time_o = [(i-1)/ 3600 for i in range(len(actual1))]
# time_o -= 6  # Apply time shift

# Plot
fig, ax = plt.subplots(figsize=(23, 12))
ax.plot(time_o[:len(actual1)], actual1, label="Observed", color='#95253B')
ax.plot(time1[:len(predicted1)], predicted1, label="Predicted", color='#3a7cb3')
ax.plot(time1[:len(allowed1)], allowed1, marker='.', color='none')  # invisible markers
ax.fill_between(time1[:len(predicted1)], predicted1, allowed1, color='#c4daec', alpha=0.5, label="Allowed Margin")

# Formatting
# ax.set_title(r"Morning: $\alpha = 0.1904$ , k = 6", fontsize=fsize)
ax.set_xlim(0, 12)
# ax.set_ylim(0, 100)
ax.set_xlabel("Time (h)")
ax.set_ylabel("Throughput (Kpps)")
ax.set_xticks(xticks)
# ax.set_yticks([0, 25, 50, 75, 100])
# ax.set_yticklabels(['0', '25', '50', '75', '100'])
ax.grid(True)
ax.legend(loc='upper left', fontsize=fsize - 2, frameon=True)
# ax.set_yscale('log')

plt.savefig('day.pdf')
plt.tight_layout()
plt.show()
