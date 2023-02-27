import matplotlib.pyplot as plt


# Create a Figure object with two subplots
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(10, 10))

x_values = list(range(-10,10))
y1_values = [x**3 for x in x_values]
y2_values = [3*x**2 for x in x_values]

# Plot the data on the first subplot
ax1.plot(x_values, y1_values)
ax1.set_xlabel('X-axis label')
ax1.set_ylabel('Y-axis label')
ax1.set_title('Function for x^2')

# Plot the data on the second subplot
ax2.plot(x_values, y2_values)
ax2.set_xlabel('X-axis label')
ax2.set_ylabel('Y-axis label')
ax2.set_title('Derivative')

# Adjust spacing between subplots
fig.subplots_adjust(wspace=0.4)

# Show the plot
plt.show()
