# Python - WEIGHTED MEAN AND STANDARD DEVIATIONS

from __future__ import division
import numpy as np
import math


# Enter the values given as the components of the vector x:
x = np.array([100.1, 100.2, 99.8, 100.3, 99.9, 100.2, 99.9, 100.4, 100.0, 100.3])

# Enter the corresponding weights w of the x values:
w = np.array([1, 2, 3, 4, 5, 5, 4, 3, 2, 1])

# Evaluation
N = len(x)
wmean = np.average(x, weights=w)
variance = np.average((x-wmean)**2, weights=w) 
stdev = math.sqrt(variance)

# Results
print ("N:", N)
print ("Weighted mean:", wmean)
print ("Weighted standard deviation of the sample:", stdev)
print ("Weighted standard deviation of the mean:", stdev/math.sqrt(N-1))

