# BINOMIAL DISTRIBUTION - VALUES and HISTOGRAM

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import binom

# Enter the following values
n = 10		# number of trials
p = 0.2		# probability of success

# Create a vector x with the values 0 ... n
x = np.array(range(0, n + 1, 1))

# The function binom.pmf(x, n, p) returns the probabilities for all x values of the
# binomial distribution with total number of attempts n and probability of
# success p. The probability mass function (pmf) is equivalent to R's dbinom function.
# We find:

dbinom = binom.pmf(x, n, p)

# Create a bar plot of these probabilities

plt.bar(x, dbinom, align="center")
plt.xlabel('Number of successes, x, in n attempts')
plt.ylabel('Probability on x successes in n attempts')
plt.xticks(x)
plt.show()


