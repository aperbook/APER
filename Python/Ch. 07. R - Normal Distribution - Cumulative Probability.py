# NORMAL DISTRIBUTION - CUMULATIVE PROBABILITY
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html
from scipy.stats import norm

# Enter the following values
mean = 4	# the mean
stdev = 1	# and standard deviation of the distribution

# Enter the value, a, of the upper limit of x:
a = 3		

print norm.cdf(a, mean, stdev)

