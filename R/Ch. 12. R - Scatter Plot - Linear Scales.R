# R - SCATTER PLOT - LINEAR SCALES

# Enter the data for the t and z vectors:
t <- c(0, 5, 10, 15, 20, 25, 30, 35, 40, 45)
z <- c(0, 12, 55, 100, 200, 305, 380, 430, 485, 490)

# Production of the scatter plot of data with linear axes and grid:
plot(t, z, pch=20, xlab="t (s)", ylab="z (m) or 10õ (m/s) or 100a (m/s^2)", xlim=c(0,50), ylim=c(-200, 600), grid())
# pch=20 gives the size of the dots used, xlab="t (s)" and ylab="z (m) or 10õ (m/s) or 100a (m/s^2)" 
# give the labels of the X-Axis and Y-Axis and xlim=c(0,50) and ylim=c(-200, 600) give the range
# of values of the two axes respectively. grid() ensures that a grid is drawn.

# ENTER returns the required scatter plot.


# THE FOLLOWING COMMANDS ARE OPTIONAL AND ADD VARIOUS FEATURES TO THE PLOT:

# Least-squares curve fit (polynomial of 4th degree):
nls(z~a0+a1*t+a2*t^2+a3*t^3+a4*t^4, start=list(a0=1, a1=1, a2=1, a3=1, a4=1))

# Plot the least-squares curve z(t). Note the use of x as variable instead of t:
curve(3.374-4.355*x+1.054*x^2-0.01774*x^3+3.986e-05*x^4, from=0, to=50, add=T, col="red")
# from=0, to=50 sets the range of the x (i.e. t) axis. col="red" sets the color of the line to red.

# Add two curves to the plot, which we will label 10õ and 100a, respectively. These happen to be
# the 10 times the first and a hundred times the second derivative of z(t), respectively,
# i.e. 10 times the velocity õ and a hundred times the acceleration a, respectively: 
curve(-43.55+21.08*x-0.5322*x^2+0.001594*x^3, from=0, to=50, add=T, col="blue")
curve(210.8-10.644*x+0.04783*x^2, from=0, to=50, add=T, col="black")

# Add labels to the three curves:
text(35, 500, "z", cex=1)
text(30, 200, "10õ", cex=1)
text(25, 20, "100a", cex=1)

