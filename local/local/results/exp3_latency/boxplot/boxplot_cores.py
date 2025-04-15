import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

# Function to read the latency data from a text file, excluding the first 100 lines
def read_latency_data(file_path):
    with open(file_path, 'r') as file:
        # Read all lines, strip any extra whitespace, and convert them to integers
        data = [int(line.strip()) for line in file.readlines()]
    
    # Exclude the first 100 lines of the data
    data = data[100:]
    
    # Convert the data from nanoseconds to microseconds (1 microsecond = 1000 nanoseconds)
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
    print(f"Minimum latency: {min_value:.2f} µs")
    print(f"Maximum latency: {max_value:.2f} µs")
    print(f"Mean latency: {mean_value:.2f} µs")
    print(f"Median latency: {median_value:.2f} µs")
    print(f"Standard deviation: {std_dev:.2f} µs")
    
    return mean_value, median_value  # Return mean and median values for plotting

# Function to plot multiple box plots side by side for each file
def plot_latency_boxplots(file_paths):
    fig, axes = plt.subplots(1, 8, figsize=(15, 6))  # 1 row, 8 columns for 8 box plots
    
    # Iterate through each file
    for i, file_path in enumerate(file_paths):
        data = read_latency_data(file_path)
        mean_value, median_value = calculate_statistics(data)
        
        # Plot boxplot for the current data
        sns.boxplot(data=data, ax=axes[i], color="lightblue",showmeans=True)

        if i == 0:
            axes[i].set_ylabel('Latency (µs)')  # Label in microseconds
            axes[i].set_title(f'{i+1} core')
        else:
            axes[i].set_title(f'{i+1} cores')
            axes[i].set_ylim(0, 150)
        
        axes[i].grid(True)
        axes[i].legend().set_visible(False)

    # Adjust layout to avoid overlap
    plt.tight_layout()
    fig.savefig('boxplot.pdf')
    plt.show()

# Main function to process multiple files and create the box plots
def analyze_latency(files_list):
    plot_latency_boxplots(files_list)

# Example usage (replace these with your actual file paths)
file_paths = ['1.txt', '2.txt', '3.txt', 
              '4.txt', '5.txt', '6.txt', 
              '7.txt', '8.txt']

analyze_latency(file_paths)
