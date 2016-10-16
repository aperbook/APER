POISSON DISTRIBUTION - VALUES and HISTOGRAM

# Enter the value of the mean ì of the distribution:

mean = 10

# Values of x (non-negative integers) to be used:

x <- seq(from = 0, to = 3*mean, by = 1)
  
# The function dpois(x, mean, log = FALSE) returns the probabilities for all x values of the Poisson distribution:   
  
dpois(x, mean, log = FALSE)

#We create a bar plot of these probabilities:

barplot(dpois(x, mean, log = FALSE), names.arg=x, xlab="Number of events ,x", ylab="Probability on x events")





