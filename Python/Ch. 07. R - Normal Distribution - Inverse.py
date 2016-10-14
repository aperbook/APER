# NORMAL DISTRIBUTION - INVERSE
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html
from scipy.stats import norm

# Enter the following values
mean = 4	# the mean
stdev = 1	# and standard deviation of the distribution

# Enter the value of the cumulative probability, p:
p = 0.6

# The value of x at which the cumulative probability is equal to p is:
print norm.ppf(p, mean, stdev)


