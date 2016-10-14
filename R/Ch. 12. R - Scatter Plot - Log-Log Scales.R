# R - SCATTER PLOT - LOG-LOG SCALES

# Enter the data for the t and z vectors:
t <- c(1, 5, 10, 15, 20, 25, 30, 35, 40, 45)
z <- c(1, 12, 55, 100, 200, 305, 380, 430, 485, 490)

# Production of the scatter plot of data with linear axes and grid:
plot(t, z, log="xy", pch=20, xlab="t (s)", ylab="z (m)", xlim=c(1,50), ylim=c(1, 1000), grid())

# pch=20 gives the size of the dots used, xlab="t (s)" and ylab="z (m)" 
# give the labels of the X-Axis and Y-Axis and xlim=c(1,50) and ylim=c(1, 1000) give the range
# of values of the two axes respectively. grid() ensures that a grid is drawn.

# ENTER returns the required scatter plot.

# Add label to the curve:
text(10, 200, "z(t)", cex=1)



# THE FOLLOWING COMMANDS ARE OPTIONAL AND ADD VARIOUS FEATURES TO THE PLOT:

# Least-squares curve fit (polynomial of 4th degree):
nls(z~a0+a1*t+a2*t^2+a3*t^3+a4*t^4, start=list(a0=1, a1=1, a2=1, a3=1, a4=1))

# Plot the least-squares curve z(t). Note the use of x as variable instead of t:
curve(9.667-6.046*x+1.184*x^2-2.149e-02*x^3+7.634e-05*x^4, from=1, to=50, add=T, col="red")
# from=1, to=50 sets the range of the x (i.e. t) axis. col="red" sets the color of the line to red.




