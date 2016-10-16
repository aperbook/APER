# Python - NORMAL DISTRIBUTION - PROBABILITY DENSITY FUNCTION

# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html
from scipy.stats import norm

# Enter the following values
mean = 4	# the mean
stdev = 1	# and standard deviation of the distribution

# Enter the value of x at which the value of the probability density function is required:
x = 3

# The value at x of the probability density function f(x) is:
print()
print("The value of the probability density at x =", x, "is f(x) =", norm.pdf(x, mean, stdev))
