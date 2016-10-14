# LEAST SQUARES FIT - PARABOLA (y = a0 + a1*x + a2*x^2)

import math
from __future__ import division
import numpy as np
import matplotlib.pyplot as plt

# Enter the values of x and the corresponding y:

x = np.array([0, 1, 2, 3, 4, 5])
y = np.array([1, 8, 20, 45, 70, 120])

# Plot, size of dots, labels, ranges of values, initial values
plt.scatter(x, y)
plt.xlabel("x, (m)")			# set the x-axis label
plt.ylabel("Displacement, y (m)")	# set the y-axis label
plt.grid(True)

# Evaluation

N = len(x)

X = sum(x)
XX = sum(x**2)
XXX = sum(x**3)
XXXX = sum(x**4)
Y = sum(y)
XY = sum(x*y)
XXY = sum(x**2*y)

DENOM = N*(XX*XXXX-XXX*XXX) - X*(X*XXXX-XX*XXX) + XX*(X*XXX-XX*XX) 
DET0 = Y*(XX*XXXX-XXX*XXX) - X*(XY*XXXX-XXX*XXY) + XX*(XY*XXX-XX*XXY)
DET1 = N*(XY*XXXX-XXX*XXY) - Y*(X*XXXX-XX*XXX) + XX*(X*XXY-XX*XY)
DET2 = N*(XX*XXY-XXX*XY) - X*(X*XXY-XX*XY) + Y*(X*XXX-XX*XX)

a0 = DET0/DENOM
a1 = DET1/DENOM
a2 = DET2/DENOM

d = y - a0 - a1*x - a2*x**2
S = math.sqrt(sum(d**2)/(N-3))

Da0 = S*math.sqrt(abs((XX*XXXX-XXX*XXX)/DENOM))
Da1 = S*math.sqrt(abs((N*XXXX-XX*XX)/DENOM))
Da2 = S*math.sqrt(abs((N*XX-X*X)/DENOM))

# Results
print("Value of a0: ", a0)
print("Value of a1: ", a1)
print("Value of a2: ", a2)
print("Standard error in a0: ", Da0)
print("Standard error in a1: ", Da1)
print("Standard error in a2: ", Da2)

# Plot least-squares line
xx = np.linspace(min(x), max(x), 200)
yy = a0 + a1*xx + a2*xx**2
plt.plot(xx, yy, '-')

plt.show()


