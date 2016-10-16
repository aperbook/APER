# Python - LEAST SQUARES FIT - EXPONENTIAL

import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

# Enter the values of the variables x and y:

x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.array([1, 8, 20, 45, 70, 120, 300, 350])

# Plot, size of dots, labels, ranges of values, initial values
plt.scatter(x, y)
plt.xlabel("x, (m)")			# set the x-axis label
plt.ylabel("Displacement, y (m)")	# set the y-axis label
plt.grid(True)

# Fit least-squares line
def exponenial_func(x, a, b, c):
    return a*np.exp(-b*x)+c
popt, pcov = curve_fit(exponenial_func, x, y, p0=(1, 1e-6, 1))

# Print coefficients
print()
print("Fitted equation: y = a * exp(-b*x) + c")
print()
print(" a =", popt[0])
print(" b =", popt[1])
print(" c =", popt[2])

xx = np.linspace(min(x), max(x), 200)
yy = exponenial_func(xx, *popt)
plt.plot(xx, yy, '-')

plt.show()

