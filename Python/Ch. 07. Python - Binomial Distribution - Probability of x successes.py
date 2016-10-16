# Python - BINOMIAL DISTRIBUTION - PROBABILITY of x SUCCESSES

# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html
from scipy.stats import binom

n = 10          # number of trials
p = 0.2         # probability of success 
x = 5           # number of successes

print ("The probability of x =", x, "successes is", binom.cdf(x, n, p))