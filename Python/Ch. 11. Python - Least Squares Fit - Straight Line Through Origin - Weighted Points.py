# Python - LEAST SQUARES FIT - STRAIGHT LINE THROUGH ORIGIN - WEIGHTED POINTS (y = b*x)

from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt

# Enter the values of x, y and their corresponding weights w:

x = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9])
y = np.array([0, 3, 6, 7, 9, 15, 17, 20, 25, 30])
w = np.array([1, 1, 2, 4, 5, 5, 2, 2, 1, 2])

# Plot, size of dots, labels, ranges of values, initial values
plt.scatter(x, y)
plt.xlabel("x, (m)")			# set the x-axis label
plt.ylabel("Displacement, y (m)")	# set the y-axis label
plt.grid(True)

# Evaluation

N = len(x)

WXX = sum(w*x**2)
WXY = sum(w*x*y)

b = WXY/WXX

d = y - b*x

WDD = sum(w*d**2)

Db = math.sqrt(WDD/((N-1)*WXX))

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


