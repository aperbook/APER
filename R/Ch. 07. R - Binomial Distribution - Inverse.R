# BINOMIAL DISTRIBUTION - INVERSE

# The Binomial Distribution Bin(n, p) is characterized by the number n of attempts 
# and the probability p of success:

# It is requird to find the smallest value x such that F(x) >= q, 
# where F is the distribution function.

# Enter the values of n, p and q:

p = 0.2
n = 15
q = 0.8

x = qbinom(p, n, q)
x