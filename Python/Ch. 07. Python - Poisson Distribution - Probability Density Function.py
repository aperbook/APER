# Python - POISSON DISTRIBUTION - PROBABILITY DENSITY FUNCTION

# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html
from scipy.stats import poisson

# Enter the value of the mean of the distribution:
mean = 10

# Enter the value of x (integer) at which the value of the density function is required:
x = 6

# The value at x of the probability density function f(x) is:
print()
print ("The value of the probability density function at x =", x, "is f(x) =", poisson.pmf(x, mean))


