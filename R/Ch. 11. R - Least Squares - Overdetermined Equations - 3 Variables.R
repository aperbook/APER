# LEAST SQUARES - OVERDETERMINED EQUATIONS - 3 VARIABLES (ax + by + cz = h)

# Enter the values of the coefficients a, b, c and h:

a <- c(1, 2, 3, 4) 
b <- c(2, 3, 4, 2)
c <- c(3, 3, -1, -3)
h <- c(14.1, 17.1, 8.1, -1.1)

# Evaluation

N <- max(length(a), length(b), length(c), length(h))

AA = sum(a^2)
BB = sum(b^2)
CC = sum(c^2)
AB = sum(a*b)
AC = sum(a*c)
AH = sum(a*h)
BC = sum(b*c)
BH = sum(b*h)
CH = sum(c*h)

DENOM = AA*(BB*CC-BC*BC) - AB*(AB*CC-AC*BC) + AC*(AB*BC-AC*BB) 
DETX = AH*(BB*CC-BC*BC) - AB*(BH*CC-BC*CH) + AC*(BC*BH-BB*CH)
DETY = AA*(BH*CC-BC*CH) - AH*(AB*CC-AC*BC) + AC*(AB*CH-AC*BH)
DETZ = AA*(BB*CH-BC*BH) - AB*(AB*CH-AC*BH) + AH*(AB*BC-AC*BB)

x = DETX/DENOM
y = DETY/DENOM
z = DETZ/DENOM

d = x*a + y*b +z*c - h
S = sqrt(sum(d^2)/(N-3))

DX = S*sqrt(abs((BB*CC-BC*BC)/DENOM))
DY = S*sqrt(abs((AA*CC-AC*AC)/DENOM))
DZ = S*sqrt(abs((AA*BB-AB*AB)/DENOM))

# Results

# Value of x:
x

# Value of y:
y

# Value of z:
z

# Standard error in x:
DX

# Standard error in y:
DY

# Standard error in z:
DZ


