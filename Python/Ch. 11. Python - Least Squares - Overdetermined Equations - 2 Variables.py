# Python - LEAST SQUARES - OVERDETERMINED EQUATIONS - 2 VARIABLES (ax + by = h)

from __future__ import division
import math
import numpy as np

# Enter the values of the coefficients a, b and h:

a = np.array([1, 2, 1, 3]) 
b = np.array([1, -1, -1, 2])
h = np.array([5.3, 0.8, -0.6, 11.2])

# Evaluation

AA = sum(a**2)
BB = sum(b**2)
AB = sum(a*b)
AH = sum(a*h)
BH = sum(b*h)

DENOM = AA*BB-AB*AB
DETX = AH*BB-AB*BH
DETY = BH*AA-AB*AH

x = DETX/DENOM
y = DETY/DENOM

d = x*a + y*b - h
S = math.sqrt(sum(d**2)/2)

DX = S*math.sqrt(BB/DENOM)
DY = S*math.sqrt(AA/DENOM)

# Results
print()
print("Equations ax + by = h")
print()
print("Value of x:", x)
print("Value of y:", y)
print("Standard error in x:", DX)
print("Standard error in y:", DY)



