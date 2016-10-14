# LEAST SQUARES FIT - STRAIGHT LINE - WEIGHTED POINTS (y = a + ë*x)

# Enter the values of x, y and their corresponding weights w:

x <- c(0, 0.2, 0.4, 0.6, 0.8, 1, 1.2, 1.4, 1.6) 
y <- c(0.92, 1.48, 1.96, 2.27, 2.61, 3.18, 3.8, 4.01, 4.85)
w <- c(1, 2, 2, 1, 6, 4, 1, 8, 5)

# Plot, size of dots, labels, ranges of values, initial values
plot(x, y, pch=20, xlab="x, (m)", ylab="Displacement, y (m)")

# Evaluation

N <- length(x)

W = sum(w)
WX = sum(w*x)
WXX = sum(w*x^2)
WY = sum(w*y)
WXY = sum(w*x*y)

DENOM = W*WXX-(WX)^2 
DETA = WY*WXX-WX*WXY
DETL = W*WXY-WX*WY

a = DETA/DENOM
ë = DETL/DENOM

d <- y - a - ë*x

WDD = sum(w*d^2)

Da = sqrt((WDD*WXX)/((N-2)*DENOM))
Dë = sqrt((WDD*W)/((N-2)*DENOM))

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



