# R - MEAN AND STANDARD DEVIATIONS

# Enter the values given as the components of the vector x:

x <- c(100.1, 100.2, 99.8, 100.3, 99.9, 100.2, 99.9, 100.4, 100.0, 100.3)

#Evaluation

N = length(x)
mean.x = mean(x)
mean.abs.dev.mean = sum(abs(x-mean.x))/N
st.dev.sample = sd(x)*sqrt((N-1)/N)
st.dev.mean = sd(x)*sqrt(1/N)

#Results

N
mean.x
mean.abs.dev.mean
st.dev.sample
st.dev.mean
