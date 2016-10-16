# Python - COLUMN AND LABEL

import numpy as np
import matplotlib.pyplot as plt

# Enter the data for the chart:
x = ('A', 'B',  'C', 'D', 'E')     # names of groups
y = [7, 12, 28, 15, 41]            # values in each group

# Plot the bar chart:
x_pos = np.arange(len(x))
plt.bar(x_pos, y, align="center")
plt.xlabel('Group Name')
plt.ylabel('Frequency')
plt.xticks(x_pos, x)
plt.show()


