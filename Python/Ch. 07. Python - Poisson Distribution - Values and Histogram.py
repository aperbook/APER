# Python - POISSON DISTRIBUTION - VALUES and HISTOGRAM

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Enter the value of the mean of the distribution:
mean = 10

# Values of x (non-negative integers) to be used (0...3*mean):
x = np.array(range(0, 3 * mean + 1, 1))

# The function pmf(x, mean) returns the probabilities for all x values of the Poisson distribution:
dpois = poisson.pmf(x, mean)

# Create a bar plot of these probabilities
plt.bar(x, dpois, align="center")
plt.xlabel('Number of events, x')
plt.ylabel('Probability on x events')
plt.xticks(x)
plt.show()

print("Values of the probabilities:")
dpois

