# LEAST SQUARES FIT - CUBIC

# Enter the values of the variables x and y:

x <- c(0, 1, 2, 3, 4, 5, 6)
y <- c(1, 8, 20, 45, 70, 120, 120)

# Plot, size of dots, labels, ranges of values, initial values
plot(x, y, pch=20, xlab="x, (m)", ylab="Displacement, y (m)")

# Fit least-squares line

fit = nls(y~A+B*x+C*x^2+D*x^3, start=list(A=1, B=1, C=1, D=1))

summary(fit)


# Plot least-squares line  
new = data.frame(x = seq(min(x),max(x), len=200))
lines(new$x, predict(fit, newdata=new))




