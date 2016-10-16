# Python - SCATTER PLOT - LOG-LOG SCALES

import numpy as np
import matplotlib.pyplot as plt

# Enter the data for the t and z vectors:
t = np.array([1, 5, 10, 15, 20, 25, 30, 35, 40, 45])
z = np.array([1, 12, 55, 100, 200, 305, 380, 430, 485, 490])

plt.scatter(t, z)
plt.xscale('log')	# the x-axis should use a logarithmic scale
plt.yscale('log')	# the y-axis should use a logarithmic scale
plt.xlim(0.5, 100)		# set the x-axis range of values
plt.ylim(0.5, 1000)	# set the y-axis range of values
plt.xlabel("t (s)")	# set the x-axis label
plt.ylabel("z (m)")	# set the y-axis label
plt.grid(True)


# Least-squares curve fit (polynomial of 4th degree - the degree may be changed)
fit = np.polyfit(t, z, 4)
p = np.poly1d(fit)

xp = np.linspace(min(t), max(t), 200)

plt.plot(xp, p(xp), '-', color="red")

plt.show()

