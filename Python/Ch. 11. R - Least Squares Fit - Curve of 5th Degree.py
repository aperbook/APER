# LEAST SQUARES FIT - CURVE OF THE 5th DEGREE

import numpy as np
import matplotlib.pyplot as plt

# Enter the values of the variables x and y:
x = np.array([0, 1, 2, 3, 4, 5, 6, 7])
y = np.array([1, 4, 15, 30, 35, 120, 170, 400])

# Plot, size of dots, labels, ranges of values, initial values
plt.scatter(x, y)
plt.xlabel("x, (m)")			# set the x-axis label
plt.ylabel("Displacement, y (m)")	# set the y-axis label
plt.grid(True)


# Fit least-squares line
fit = np.polyfit(x, y, 5)

# Print coefficients
print("Fit: y = A + B*x + C*x^2 + D*x^3 + E*x^4 + F*x^5")
print(" A = ", fit[5])
print(" B = ", fit[4])
print(" C = ", fit[3])
print(" D = ", fit[2])
print(" E = ", fit[1])
print(" F = ", fit[0])

p = np.poly1d(fit)
xp = np.linspace(min(x), max(x), 200)
plt.plot(xp, p(xp), '-')

plt.show()

