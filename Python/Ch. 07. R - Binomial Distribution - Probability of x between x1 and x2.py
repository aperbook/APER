# R - BINOMIAL DISTRIBUTION - PROBABILITY of x BETWEEN x1 and x2
# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.binom.html

from scipy.stats import binom

# Enter the following values
n = 10          # number of trials
p = 0.2         # probability of success 
x1 = 3          # minimum number of successes
x2 = 7          # maximum number of successes

print binom.cdf(x2, n, p) - binom.cdf(x1, n, p) +  binom.pmf(x1, n, p)
