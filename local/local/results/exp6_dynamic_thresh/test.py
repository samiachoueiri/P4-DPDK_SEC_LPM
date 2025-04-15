import matplotlib.pyplot as plt
import numpy as np

# Generate sample data
x = np.linspace(0, 10, 100)  # x values
y = np.sin(x)  # y values (you can use any function)

# Define the range of y-values to shade
y_min = -0.5
y_max = 0.5

# Plot the function (optional)
plt.plot(x, y, label='y = sin(x)', color='blue')

# Shade the area between y_min and y_max
plt.fill_between(x[0:4], y_min, y_max, color='orange', alpha=0.3, label='Shaded Area')

# Adding labels and title
plt.title('Shading an Area in a Graph')
plt.xlabel('x')
plt.ylabel('y')

# Show legend
plt.legend()

# Display the plot
plt.show()
