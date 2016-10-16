# Python - LEAST SQUARES FIT - CUBIC

import numpy as np
import matplotlib.pyplot as plt

# Enter the values of the variables x and y:
x = np.array([0, 1, 2, 3, 4, 5, 6])
y = np.array([1, 8, 20, 45, 70, 120, 120])

# Plot, size of dots, labels, ranges of values, initial values
plt.scatter(x, y)
plt.xlabel("x, (m)")			# set the x-axis label
plt.ylabel("Displacement, y (m)")	# set the y-axis label
plt.grid(True)


# Fit least-squares line
fit = np.polyfit(x, y, 3)

# Print coefficients
print()
print("Fitted equation: y = A + B*x + C*x^2 + D*x^3")
print()
print(" A =", fit[3])
print(" B =", fit[2])
print(" C =", fit[1])
print(" D =", fit[0])

p = np.poly1d(fit)
xp = np.linspace(min(x), max(x), 200)
plt.plot(xp, p(xp), '-')

plt.show()
