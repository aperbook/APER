# Python - NORMAL DISTRIBUTION - INVERSE

# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.norm.html
from scipy.stats import norm

# Enter the following values
mean = 4	# the mean
stdev = 1	# and standard deviation of the distribution

# Enter the value of the cumulative probability, P:
P = 0.6

# Evaluation:
# The value of x at which the cumulative probability is equal to P is:
x0 = norm.ppf(P, mean, stdev)

# Result:
print ()
print ("The value of x for which the cumulative probability\nis equal to P =", P, "is x0 =", x0)

