import matplotlib.pyplot as plt
import numpy as np

# Sample data
x = np.linspace(0, 10, 100)
y1 = np.sin(x)
y2 = np.cos(x)

# Create the figure and axes with 1 row and 2 columns (side by side)
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(12, 6))

# Plot the first curve (sin(x)) on the first subplot
ax1.plot(x, y1, label='sin(x)', color='blue')
ax1.set_title('Sine Curve')
ax1.set_xlabel('x')
ax1.set_ylabel('sin(x)')
ax1.grid(True)
ax1.legend()

# Plot the second curve (cos(x)) on the second subplot
ax2.plot(x, y2, label='cos(x)', color='red')
ax2.set_title('Cosine Curve')
ax2.set_xlabel('x')
ax2.set_ylabel('cos(x)')
ax2.grid(True)
ax2.legend()

# Adjust spacing between subplots
plt.tight_layout()

# Show the plot
plt.show()

