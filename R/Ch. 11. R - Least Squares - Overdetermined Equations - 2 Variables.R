# LEAST SQUARES - OVERDETERMINED EQUATIONS - 2 VARIABLES (ax + by = h)

# Enter the values of the coefficients a, b and h:

a <- c(1, 2, 1, 3) 
b <- c(1, -1, -1, 2)
h <- c(5.3, 0.8, -0.6, 11.2)

# Evaluation

AA = sum(a^2)
BB = sum(b^2)
AB = sum(a*b)
AH = sum(a*h)
BH = sum(b*h)

DENOM = AA*BB-AB*AB
DETX = AH*BB-AB*BH
DETY = BH*AA-AB*AH

x = DETX/DENOM
y = DETY/DENOM

d = x*a + y*b - h
S = sqrt(sum(d^2)/2)

DX = S*sqrt(BB/DENOM)
DY = S*sqrt(AA/DENOM)

# Results

# Value of x:
x

# Value of y:
y

# Standard error in x:
DX

# Standard error in y:
DY

