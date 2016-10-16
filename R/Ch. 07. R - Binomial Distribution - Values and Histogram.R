BINOMIAL DISTRIBUTION - VALUES and HISTOGRAM

# Enter the following values:

number.of.trials = 10
probability.of.success = 0.2

# Evaluation

n = number.of.trials
p = probability.of.success
x <- (0:n)

# The function dbinom(x, n, p) returns the probabilities for all x values of the binomial distribution with total number of attempts n and probability of success p. We find:   
  
dbinom(x,n,p)

#We create a bar plot of these probabilities:

barplot(dbinom(x,n,p), names.arg=x, xlab="Number of successes, x, in n attempts", ylab="Probability on x successes in n attempts")





