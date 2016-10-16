# Python - NORMAL DISTRIBUTION - PROBABILITY OF x BETWEEN x1 AND x2

# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html
from scipy.stats import norm

# Enter the following values
mean = 4	# the mean
stdev = 1	# and standard deviation of the distribution

# Enter the values of the limits of x:
x1 = 3
x2 = 5

# Evaluation of the probability of a value of x between x1 and x2 is:
p = norm.cdf(x2, mean, stdev) - norm.cdf(x1, mean, stdev)

# Result:
print()
print("The probability of a value of x between x1 =", x1, "and x2 =", x2, "is p =", p)