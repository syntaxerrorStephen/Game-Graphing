import matplotlib.pyplot as plt
import csv

# Define the input and output file paths
input_file = 'punch_data.csv'
output_file = 'punch_chart.svg'

# Initialize the round and punch counters
current_round = 0
punch_count = 0
punch_counts = []

# Read the punch data from the CSV file
with open(input_file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
        # Check if a new round has started
        if int(row[0]) > current_round:
            # Save the total punch count for the previous round
            punch_counts.append(punch_count)
            # Reset the punch counter for the new round
            punch_count = 0
            current_round = int(row[0])
        # Count the punch if it was registered
        if row[1] != '0':
            punch_count += 1

# Create the bar chart
fig, ax = plt.subplots()
ax.bar(range(len(punch_counts)), punch_counts)
ax.set_xlabel('Round')
ax.set_ylabel('Punches')
ax.set_title('Total Punches per Round')

# Save the chart as an SVG file
fig.savefig(output_file, format='svg')
