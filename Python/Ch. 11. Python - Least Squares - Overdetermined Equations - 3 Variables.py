# Python - LEAST SQUARES - OVERDETERMINED EQUATIONS - 3 VARIABLES (ax + by + cz = h)

from __future__ import division
import math
import numpy as np

# Enter the values of the coefficients a, b, c and h:
a = np.array([1, 2, 3, 4])
b = np.array([2, 3, 4, 2])
c = np.array([3, 3, -1, -3])
h = np.array([14.1, 17.1, 8.1, -1.1])

# Evaluation
N = max(len(a), len(b), len(c), len(h))

AA = sum(a**2)
BB = sum(b**2)
CC = sum(c**2)
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
S = math.sqrt(sum(d**2)/(N-3))

DX = S*math.sqrt(abs((BB*CC-BC*BC)/DENOM))
DY = S*math.sqrt(abs((AA*CC-AC*AC)/DENOM))
DZ = S*math.sqrt(abs((AA*BB-AB*AB)/DENOM))

# Results
print()
print("Equations: ax + by + cz = h")
print()
print("Value of x:", x)
print("Value of y:", y)
print("Value of z:", z)
print("Standard error in x:", DX)
print("Standard error in y:", DY)
print("Standard error in z:", DZ)

