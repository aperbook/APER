# R - BINOMIAL DISTRIBUTION - PROBABILITY of x BETWEEN x1 and x2

# Enter the following values:

number.of.trials = 10
probability.of.success = 0.2
minimum.number.of.successes = 3
maximum.number.of.successes = 7

# Evaluation

n = number.of.trials
p = probability.of.success
x1 = minimum.number.of.successes
x2 = maximum.number.of.successes
P = pbinom(x2, n, p)-pbinom(x1, n, p)+dbinom(x1, n, p)

# Probability P(x) that the number of successes lies between x1 and x2 (both included):      

P

