# Python - LEAST SQUARES FIT - STRAIGHT LINE (y = a + b*x)

from __future__ import division
import math
import numpy as np
import matplotlib.pyplot as plt

# Enter the values of x, y:
x = np.array([0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6])
y = np.array([0.92, 1.48, 1.96, 2.27, 2.61, 3.18, 3.8, 4.01, 4.85])

# Plot, size of dots, labels, ranges of values, initial values
plt.scatter(x, y)
plt.xlabel("x, (m)")			# set the x-axis label
plt.ylabel("Displacement, y (m)")	# set the y-axis label
plt.grid(True)

# Evaluation

N = len(x)
X = sum(x)
XX = sum(x**2)
Y = sum(y)
XY = sum(x*y)

DENOM = N*XX-X**2 
DETA = Y*XX-X*XY
DETL = N*XY-X*Y

a = DETA/DENOM
b = DETL/DENOM

d = y - a - b*x

DD = sum(d**2)

Da = math.sqrt((DD*XX)/((N-2)*DENOM))
Db = math.sqrt((N*DD)/((N-2)*DENOM))

# Results
print()
print("Fitted equation: y = a + bx")
print()
print("Value of a:", a)
print("Value of b:", b)
print("Standard error in a:", Da)
print("Standard error in b:", Db)

# Plot least-squares line  
xx = np.linspace(min(x), max(x), 200)
yy = a + b * xx
plt.plot(xx, yy, '-')

plt.show()



