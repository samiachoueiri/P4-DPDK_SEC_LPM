import matplotlib.pyplot as plt

# Load data from the text file
with open('day_20240619.txt', 'r') as file:
    data = [float(line.strip()) for line in file]

# Print values > 40000 with their index
for i, value in enumerate(data):
    if value > 20000:
        print(f"Index: {i}, Value: {value}")
        
# # Create a time axis (assuming measurements every second)
# time = list(range(len(data)))  # or use numpy: np.arange(len(data))

# Create a time axis in hours
time_hours = [i / 3600 for i in range(len(data))]

# Plot the signal
plt.figure(figsize=(12, 6))
plt.plot(time_hours, data, label='Signal')
# plt.xlim(0,24)
# plt.xticks([0, 3, 6, 9, 12, 15, 18, 21, 24])
xticks = range(0, int(time_hours[-1]) + 1, 1)  # ticks every hour
plt.xticks(xticks)
plt.xlabel('Time (seconds)')
plt.ylabel('Measurement')
plt.title('Signal Over Time')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
