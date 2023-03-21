# Punch Chart Generator V2

**The Punch Chart Generator is a Python script that reads punch data from a CSV file and generates a bar chart of the total punches per round using the matplotlib library. The resulting chart is saved as an SVG file.**

## Prerequisites

To run the Punch Chart Generator, you need to have Python 3 and the following libraries installed:

1. matplotlib
2. csv

## Input Format

The input data for the Punch Chart Generator should be in a CSV file with the following format:

```
round_number, punch_count
round_number, punch_count
round_number, punch_count
...
```

Each row represents a round of the boxing game, with the round number and the number of punches registered in that round separated by a comma. The script assumes that the data is sorted by round number in ascending order.
