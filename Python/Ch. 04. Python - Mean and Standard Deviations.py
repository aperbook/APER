# Python - MEAN AND STANDARD DEVIATIONS

from __future__ import division
import numpy as np
import math

# Enter the values given as the components of the vector x:
x = np.array([100.1, 100.2, 99.8, 100.3, 99.9, 100.2, 99.9, 100.4, 100.0, 100.3])

N = len(x)
mean_x = x.mean()
mean_abs_dev_mean = np.sum(np.abs(x-mean_x)) / N
std_dev_sample = x.std(ddof = 1) * math.sqrt((N-1)/N)
std_dev_mean = x.std(ddof = 1) * math.sqrt(1/N)

print ("Number of values N =", N)
print ("Mean =", mean_x)
print ("Standard deviation of the sample =", std_dev_sample)
print ("Standard deviation of the mean =", std_dev_mean)
