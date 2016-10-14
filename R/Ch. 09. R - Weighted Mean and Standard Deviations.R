# WEIGHTED MEAN AND STANDARD DEVIATIONS

# Enter the values given as the components of the vector x:

x <- c(100.1, 100.2, 99.8, 100.3, 99.9, 100.2, 99.9, 100.4, 100.0, 100.3)

# Enter the corresponding weights w of the x values:

w <- c(1, 2, 3, 4, 5, 5, 4, 3, 2, 1)

# Evaluation

N = length(x)
wmean <- weighted.mean(x, w)
variance <- weighted.mean((x-wmean)^2, w)
stdev <- sqrt(variance)

# Results

# N
N

# Weighted mean
wmean

# Standard deviation of the sample
stdev

# Standard deviation of the mean
stdev/sqrt(N-1)






