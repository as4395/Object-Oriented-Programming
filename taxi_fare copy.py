# This script explores three different methods of the matplotlib package 

import matplotlib.pyplot as plt

def create_line_plot(x, y):
    """This function creates a line plot using matplotlib."""
    plt.plot(x, y)  # Method 1: plt.plot()
    plt.title("Line Plot Example")
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.show()

# Data structure: List
x = [1, 2, 3, 4, 5]  # X-axis values
y = [2, 4, 6, 8, 10]  # Y-axis values
create_line_plot(x, y)  # Call the user-defined function