# COLUMN AND LABEL

# Enter the data for the chart:

x <- c("A", "B",  "C", "D", "E")
y <- c(7, 12, 28, 15, 41)

# Plot the bar chart:

barplot(y, names.arg = x , xlab = "Group Name", ylab = "Total Number of Marks", col = "gray", 
        main = "Group Performance")




