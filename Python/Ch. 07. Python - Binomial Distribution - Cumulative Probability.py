# Python - BINOMIAL DISTRIBUTION - CUMULATIVE PROBABILITY

# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html
from scipy.stats import binom

# Enter the following values

n = 10          # number of trials
p = 0.5         # probability of success 
x = 5           # maximum number of successes


print ("Cumulative probability up to x =", x, "is", binom.cdf(x, n, p))