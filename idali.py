import matplotlib.pyplot as plt

# Example threshold values (replace this with your actual data)
threshold_values = [0.1, 0.2, 0.5, 0.3, 0.7, 0.8, 0.4, 0.6, 0.2, 0.5, 0.6, 0.4]

# Plot histogram
plt.hist(threshold_values, bins=10, edgecolor='black')  # Adjust number of bins as needed
plt.title('Histogram of Threshold Values')
plt.xlabel('Threshold Values')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()
