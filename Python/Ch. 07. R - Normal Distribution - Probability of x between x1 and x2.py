# NORMAL DISTRIBUTION - PROBABILITY OF x BETWEEN x1 AND x2
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html
from scipy.stats import norm

# Enter the following values
mean = 4	# the mean
stdev = 1	# and standard deviation of the distribution

# Enter the values of the limits of x:
x1 = 3
x2 = 5

# The value at x of the probability density function f(x) is:
print norm.cdf(x2, mean, stdev) - norm.cdf(x1, mean, stdev)

