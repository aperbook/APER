# COLUMN AND LABEL

import numpy as np
import matplotlib.pyplot as plt

# Enter the data for the chart:
x = ('A', 'B',  'C', 'D', 'E')     # groups
y = [7, 12, 28, 15, 41]            # values

# Plot the bar chart:
x_pos = np.arange(len(x))
plt.bar(x_pos, y, align="center")
plt.xlabel('Group Name')
plt.ylabel('Total Number of Marks')
plt.xticks(x_pos, x)
plt.show()


