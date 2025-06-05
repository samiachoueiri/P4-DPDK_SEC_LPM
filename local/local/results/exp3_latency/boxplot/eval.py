import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Function to read the latency data from a text file and return a list of values
def read_latency_data(file_path):
    with open(file_path, 'r') as file:
        # Read lines, strip any extra whitespace and convert each line to an integer
        data = [int(line.strip()) for line in file.readlines()]
        data = data[100:]
        data = [value / 1000 for value in data]
    return data

# Function to calculate and print statistics
def calculate_statistics(data):
    min_value = np.min(data)
    max_value = np.max(data)
    mean_value = np.mean(data)
    median_value = np.median(data)
    std_dev = np.std(data)
    sample_count = len(data)
    
    print(f"Number of samples: {sample_count}")
    print(f"Minimum latency: {min_value}")
    print(f"Maximum latency: {max_value}")
    print(f"Mean latency: {mean_value:.2f}")
    print(f"Median latency: {median_value}")
    print(f"Standard deviation: {std_dev:.2f}")

    return mean_value, median_value  # Return mean and median values for plotting

def plot_latency_boxplot(data):
    plt.figure(figsize=(8, 6))
    sns.boxplot(data=data, color="lightblue",showmeans=True)

    plt.title('Latency Distribution Box Plot')
    plt.ylabel('Latency (µs)')  # Label in microseconds
    plt.legend()  # Show legend
    plt.grid(True)
    plt.show()

# Main function to process the file and create the box plot
def analyze_latency(file_path):
    data = read_latency_data(file_path)
    calculate_statistics(data)
    plot_latency_boxplot(data)

# Example usage (replace 'latency_data.txt' with your file path)
file_path = 'Sandia_170.txt'
analyze_latency(file_path)