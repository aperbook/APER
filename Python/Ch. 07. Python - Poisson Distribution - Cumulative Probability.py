# Python - POISSON DISTRIBUTION - CUMULATIVE PROBABILITY

# http://docs.scipy.org/doc/scipy-0.16.0/reference/generated/scipy.stats.poisson.html
from scipy.stats import poisson

# Enter the value of the mean of the distribution:
mean = 10

# Enter the value of the maximum value of x:
x = 8	

# The probability P(x) that the number of successes is less than or equal to x is:
print()
print("The cumulative probability that the number of events \nis less than or equal to x =", x, "is P(x) =", poisson.cdf(x, mean))


