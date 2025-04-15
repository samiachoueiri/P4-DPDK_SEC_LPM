import numpy as np
import matplotlib.pyplot as plt

# Load the data from the file
filename = "output_050.txt"

# Read the file and extract relevant columns
data = np.loadtxt(filename)

time = data[:, 0]  # Column 1: Time
actual_values = data[:, 3] / 1000  # Column 4: Actual values
actual_values_list = actual_values.tolist()
actual_values_list.pop()
predicted_values = data[:, 4] / 1000  # Column 5: Predicted values
predicted_values_list = predicted_values.tolist()
predicted_values_list.pop(0)
allowed_values = data[:, 5] / 1000  # Column 6: Allowed values
allowed_values_list = allowed_values.tolist()
allowed_values_list.pop(0)

# Shift the predicted values 1 unit to the left on the time axis
shifted_time = time - 1  

# Plot the signals
plt.figure(figsize=(10, 5))
plt.plot(time[0:len(actual_values_list)], actual_values_list, label="Observed", color='#95253B')
plt.plot(time[0:len(predicted_values_list)], predicted_values_list, label="Predicted",color='#3a7cb3')
plt.plot(time[0:len(allowed_values_list)], allowed_values_list, label="Allowed", marker='.',color='#3a7cb3')

# Shade the region between shifted predicted values and allowed values
plt.fill_between(time[0:len(predicted_values_list)], predicted_values_list, allowed_values_list, color='#c4daec', alpha=0.3, label="Allowed Margin")

# Labels and title
plt.xlabel("Time (s)")
# plt.xlim(-0.5,51)
plt.ylabel("Throughput (Thousand Packets per Second)")
plt.ylim(bottom=75, top=210)
plt.title("alpha = 0.5")
plt.legend()
plt.grid()

# plt.savefig("output_05.pdf")
# Show the plot
plt.show()

