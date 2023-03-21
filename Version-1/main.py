import matplotlib.pyplot as plt

# Sample data for punches landed by each boxer in each round
boxer1 = [20, 18, 15, 12, 10, 8, 6, 4, 2, 0]
boxer2 = [10, 12, 14, 16, 18, 20, 22, 24, 26, 28]

# Plot the data
fig, ax = plt.subplots()
ax.plot(range(1, 11), boxer1, label='Boxer 1')
ax.plot(range(1, 11), boxer2, label='Boxer 2')

# Set the axis labels and title
ax.set_xlabel('Round')
ax.set_ylabel('Punches Landed')
ax.set_title('Punches Landed per Round')

# Add a legend
ax.legend()

# Write the plot to an SVG file
plt.savefig('punches_landed_graph.svg')
