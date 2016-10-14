# R - SCATTER PLOT - LOG-LOG SCALES - MULTIPLE

# Enter the data for the t and z vectors:
t <- c(1, 10, 20, 30, 40, 50)
z1 <- c(1, 12, 55, 100, 200, 305)
z2 <- c(5, 20, 80, 150, 300, 400)
z3 <- c(10, 40, 100, 200, 400, 500)
z4 <- c(15, 50, 150, 300, 450, 550)

# The scatter plots:
plot(t, z1, log="xy", pch=20, xlab="t (s)", ylab="z (m)", xlim=c(0.7,100), ylim=c(0.3, 1000), grid(), col="black")
points(t, z2, log="xy", pch=20, xlab="t (s)", ylab="z (m) (m/s)", xlim=c(0.7,100), ylim=c(0.3, 1000), grid(), col="red")
points(t, z3, log="xy", pch=20, xlab="t (s)", ylab="z (m) (m/s)", xlim=c(0.7,100), ylim=c(0.3, 1000), grid(), col="green")
points(t, z4, log="xy", pch=20, xlab="t (s)", ylab="z (m) (m/s)", xlim=c(0.7,100), ylim=c(0.3, 1000), grid(), col="blue")

# Add labels to the three curves:
text(0.8, 0.7, "z1", cex=1)
text(0.8, 5, "z2", cex=1)
text(0.8, 13, "z3", cex=1)
text(0.8, 25, "z4", cex=1)


# THE FOLLOWING COMMANDS ARE OPTIONAL AND ADD VARIOUS FEATURES TO THE PLOT:

# Least-squares curves fit (polynomials of 3rd degree):
nls(z1~a0+a1*t+a2*t^2+a3*t^3, start=list(a0=1, a1=1, a2=1, a3=1))
nls(z2~b0+b1*t+b2*t^2+b3*t^3, start=list(b0=1, b1=1, b2=1, b3=1))
nls(z3~c0+c1*t+c2*t^2+c3*t^3, start=list(c0=1, c1=1, c2=1, c3=1))
nls(z4~d0+d1*t+d2*t^2+d3*t^3, start=list(d0=1, d1=1, d2=1, d3=1))

# Using the coefficients found above, we plot the least-squares curves z1, z2, z3 and z4. 
# Note the use of x as variable instead of t:
curve(0.6873536+0.1922235*x+0.1066485*x^2+0.0002363*x^3, from=0.7, to=100, add=T, col="black")
curve(9.5149-2.4712*x+0.3374*x^2-0.0026*x^3, from=0.7, to=100, add=T, col="red")
curve(20.854751-4.434922*x+0.517319*x^2-0.004672*x^3, from=0.7, to=100, add=T, col="green")
curve(18.569861-2.691005*x+0.608757*x^2-0.006839*x^3, from=0.7, to=100, add=T, col="blue")


