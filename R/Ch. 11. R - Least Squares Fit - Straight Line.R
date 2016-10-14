# LEAST SQUARES FIT - STRAIGHT LINE (y = a + ë*x)

# Enter the values of x, y:

x <- c(0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6) 
y <- c(0.92, 1.48, 1.96, 2.27, 2.61, 3.18, 3.8, 4.01, 4.85)

# Plot, size of dots, labels, ranges of values, initial values
plot(x, y, pch=20, xlab="x, (m)", ylab="Displacement, y (m)")

# Evaluation

N <- length(x)

X = sum(x)
XX = sum(x^2)
Y = sum(y)
XY = sum(x*y)

DENOM = N*XX-X^2 
DETA = Y*XX-X*XY
DETL = N*XY-X*Y

a = DETA/DENOM
ë = DETL/DENOM

d <- y - a - ë*x

DD = sum(d^2)

Da = sqrt((DD*XX)/((N-2)*DENOM))
Dë = sqrt((N*DD)/((N-2)*DENOM))

# Results

# Value of a:
a

# Value of ë:
ë

# Standard error in a:
Da

# Standard error in ë:
Dë

# Plot least-squares line  

abline(a,ë)



