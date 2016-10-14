# LEAST SQUARES FIT - PARABOLA (y = a0 + a1*x + a2*x^2)

# Enter the values of x and the corresponding y:

x <- c(0, 1, 2, 3, 4, 5) 
y <- c(1, 8, 20, 45, 70, 120)

# Plot, size of dots, labels, ranges of values, initial values
plot(x, y, pch=20, xlab="x, (m)", ylab="Displacement, y (m)")

# Evaluation

N <- length(x)

X = sum(x)
XX = sum(x^2)
XXX = sum(x^3)
XXXX = sum(x^4)
Y = sum(y)
XY = sum(x*y)
XXY = sum(x^2*y)

DENOM = N*(XX*XXXX-XXX*XXX) - X*(X*XXXX-XX*XXX) + XX*(X*XXX-XX*XX) 
DET0 = Y*(XX*XXXX-XXX*XXX) - X*(XY*XXXX-XXX*XXY) + XX*(XY*XXX-XX*XXY)
DET1 = N*(XY*XXXX-XXX*XXY) - Y*(X*XXXX-XX*XXX) + XX*(X*XXY-XX*XY)
DET2 = N*(XX*XXY-XXX*XY) - X*(X*XXY-XX*XY) + Y*(X*XXX-XX*XX)

a0 = DET0/DENOM
a1 = DET1/DENOM
a2 = DET2/DENOM

d <- y - a0 - a1*x - a2*x^2
S = sqrt(sum(d^2)/(N-3))

Da0 = S*sqrt(abs((XX*XXXX-XXX*XXX)/DENOM))
Da1 = S*sqrt(abs((N*XXXX-XX*XX)/DENOM))
Da2 = S*sqrt(abs((N*XX-X*X)/DENOM))

# Results

# Plot least-squares line  
new = data.frame(x = seq(min(x),max(x), len=200))
lines(new$x, predict(fit, newdata=new))

# Value of a0:
a0

# Value of a1:
a1

# Value of a2:
a2

# Standard error in a0:
Da0

# Standard error in a1:
Da1

# Standard error in a2:
Da2


