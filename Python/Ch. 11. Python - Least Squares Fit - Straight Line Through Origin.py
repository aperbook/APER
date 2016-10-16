# Python - LEAST SQUARES FIT - STRAIGHT LINE THROUGH ORIGIN (y = b*x)

from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt

# Enter the values of x, y:
x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([0, 3, 6, 7, 9, 15, 17, 20, 25, 30])

# Plot, size of dots, labels, ranges of values, initial values
plt.scatter(x, y)
plt.xlabel("x, (m)")			# set the x-axis label
plt.ylabel("Displacement, y (m)")	# set the y-axis label
plt.grid(True)

# Evaluation

N = len(x)

XX = sum(x**2)
XY = sum(x*y)

b = XY/XX

d = y - b*x

DD = sum(d**2)

Db = math.sqrt(DD/((N-1)*XX))

# Results
print()
print("Fitted equation: y = bx")
print()
print("Value of b:", b)
print("Standard error in b:", Db)

# Plot least-squares line  
xx = np.linspace(min(x), max(x), 200)
yy = b * xx
plt.plot(xx, yy, '-')

plt.show()

