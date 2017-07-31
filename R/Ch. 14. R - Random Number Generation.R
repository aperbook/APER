# R - RANDOM NUMBERS DISTRIBUTED ACCORDING TO A GIVEN DISTRIBUTION

-----------------------------------------------------------------------------------------------------
  
# UNIFORM DISTRIBUTION

# To obtain the histogram of N numbers distributed uniformly in the range between min and max,
# enter the numerical values of N, min and max and run the program.
# The values of the N numbers are the components of vector x.


N = 10000
min = -2
max = 1

x = runif(N, min, max)
hist(x, main=paste("Histogram of N =", N, "random numbers,\n distributed uniformly between xmin =", min, "and xmax =", max))
 
-----------------------------------------------------------------------------------------------------

# BINOMIAL DISTRIBUTION

# To obtain the histogram of N numbers distributed according to a Binomial distribution 
# with total mumber of attempts n and probability of success p,
# enter the numerical values of N, n and p and run the program.
# The values of the N numbers are the components of vector x.


N = 10000
n = 50
p = 0.2

x= rbinom(size=n, n=N, prob=p)
hist(x, main=paste("Histogram of N =", N, "random numbers distributed according to a Binomial\n distribution with number of attempts n =", n, "and probability of success p =", p))

-----------------------------------------------------------------------------------------------------
     
# POISSON DISTRIBUTION

# To obtain the histogram of N numbers distributed according to a Poisson distribution with mean ë,
# enter the numerical values of N and ë and run the program.
# The values of the N numbers are the components of vector x.
     
N = 10000
ë = 5

x = rpois(N, ë)
hist(x, main=paste("Histogram of N =", N, "random numbers distributed\n according to a Poisson distribution with mean ë =", ë))

-----------------------------------------------------------------------------------------------------
  
# NORMAL DISTRIBUTION
  
# To obtain the histogram of N numbers distributed according to a Normal distribution 
# with a mean of ì and standard deviation ó, 
# enter the numerical values of N, ì and ó and run the program.
# The values of the N numbers are the components of vector x.
  
  
N = 10000
ì = 50
ó = 1

x= rnorm(N, mean=ì, sd=ó)
hist(x, main=paste("Histogram of N =", N, "random numbers distributed according to a\n Normal distribution with mean ì =", ì, "and standard deviation ó =", ó ))

-----------------------------------------------------------------------------------------------------
  