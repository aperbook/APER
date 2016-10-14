# POISSON DISTRIBUTION - PROBABILITY DENSITY FUNCTION
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html
from scipy.stats import poisson

# Enter the value of the mean of the distribution:
mean = 10

# Enter the value of x at which the value of the density function is required:
x = 8

# The value at x of the probability density function f(x) is:
print poisson.pmf(x, mean)

