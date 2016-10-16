# Python - POISSON DISTRIBUTION - PROBABILITY of x BETWEEN x1 and x2

# http://docs.scipy.org/doc/scipy/reference/generated/scipy.stats.poisson.html
from scipy.stats import poisson

# Enter the value of the mean of the distribution:
mean = 10

# Enter the values of the limits of x (integers):
x1 = 5
x2 = 10

# Probability P(x) that the number of events lies between x1 and x2 (both included):      
print()
print("The probability that the number of events, x, lies between \nx1 =", x1, "and x2 =", x2, 
"(both included) is P(x) =", (poisson.cdf(x2, mean) - poisson.cdf(x1, mean) + poisson.pmf(x1, mean)))


