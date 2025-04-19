import matplotlib.pyplot as plt  # Importing matplotlib for data visualization

# Example 1: Creating a simple line plot
# Data structure: list
# This method demonstrates how to create a line plot using matplotlib.
x = [1, 2, 3, 4, 5]  # X-axis values (list)
y = [2, 4, 6, 8, 10]  # Y-axis values (list)
plt.plot(x, y)  # Method 1: plt.plot() for line plot
plt.title("Line Plot Example")  # Adding title
plt.xlabel("X-axis")  # Adding X-axis label
plt.ylabel("Y-axis")  # Adding Y-axis label
plt.show()  # Display the plot

# Example 2: Creating a bar chart
# Conditional statement: only create the bar chart if the data list is not empty
categories = ["A", "B", "C", "D"]
values = [10, 20, 15, 25]
if categories and values:  # Conditional to check if data exists
    plt.bar(categories, values)  # Method 2: plt.bar() for bar chart
    plt.title("Bar Chart Example")
    plt.xlabel("Categories")
    plt.ylabel("Values")
    plt.show()

# Example 3: Creating a scatter plot with a loop
# This method demonstrates creating a scatter plot using matplotlib.
# Loop: Generate data points for the scatter plot
scatter_x = []
scatter_y = []
for i in range(1, 6):  # Adding values to lists using a loop
    scatter_x.append(i)
    scatter_y.append(i**2)

plt.scatter(scatter_x, scatter_y)  # Method 3: plt.scatter() for scatter plot
plt.title("Scatter Plot Example")
plt.xlabel("X-axis (Generated)")
plt.ylabel("Y-axis (Squared Values)")
plt.show()

# Additional Data Structure: Set to store unique categories
unique_categories = set(categories)
print("Unique categories (using a set):", unique_categories)

