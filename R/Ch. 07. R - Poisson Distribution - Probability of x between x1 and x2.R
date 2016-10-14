# POISSON DISTRIBUTION - PROBABILITY of x BETWEEN x1 and x2

# Enter the value of the mean of the distribution:

mean = 10

# Enter the values of the limits of x:

x1 = 5
x2 = 10

# Probability P(x) that the number of events lies between x1 and x2 (both included):      

ppois(x2, mean, lower.tail = TRUE, log.p = FALSE) - ppois(x1, mean, lower.tail = TRUE, log.p = FALSE) + dpois(x1, mean, log = FALSE)



