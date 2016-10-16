# Python - SCATTER PLOT - LINEAR-LOG SCALES - MULTIPLE

import numpy as np
import matplotlib.pyplot as plt

# Enter the data for the t and z vectors:
t = np.array([0, 10, 20, 30, 40, 50])
z1 = np.array([0, 12, 55, 100, 200, 305])
z2 = np.array([5, 20, 80, 150, 300, 400])
z3 = np.array([10, 40, 100, 200, 400, 500])
z4 = np.array([15, 50, 150, 300, 450, 550])

# The scatter plots:
plt.scatter(t, z1, color="black")
plt.scatter(t, z2, color="red")
plt.scatter(t, z3, color="green")
plt.scatter(t, z4, color="blue")
plt.yscale('log')	# the y-axis should use a logarithmic scale
plt.xlim(0, 55)		# set the x-axis range of values
plt.ylim(1, 1000)	# set the y-axis range of values
plt.xlabel("t (s)")	# set the x-axis label
plt.ylabel("z (m)")	# set the y-axis label
plt.grid(True)


# Least-squares curve fit (polynomial of 4th degree - the degree may be changed)
fit1 = np.polyfit(t, z1, 4)
fit2 = np.polyfit(t, z2, 4)
fit3 = np.polyfit(t, z3, 4)
fit4 = np.polyfit(t, z4, 4)
p1 = np.poly1d(fit1)
p2 = np.poly1d(fit2)
p3 = np.poly1d(fit3)
p4 = np.poly1d(fit4)

xp = np.linspace(min(t), max(t), 200)

plt.plot(xp, p1(xp), '-', color="black")
plt.plot(xp, p2(xp), '-', color="red")
plt.plot(xp, p3(xp), '-', color="green")
plt.plot(xp, p4(xp), '-', color="blue")

plt.show()

