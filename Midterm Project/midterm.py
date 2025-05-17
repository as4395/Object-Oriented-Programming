# The purpose of the code is to explore three different methods of the matplotlib package
 
import matplotlib.pyplot as plt 
 
# Example 1: Line Plot 
def create_line_plot(years, revenue):
    plt.plot(years, revenue, marker='o', color='blue')  # Method: plt.plot() to create a line plot
    plt.title("Company Revenue Over Time") 
    plt.xlabel("Year")  
    plt.ylabel("Revenue (in USD Millions)")  
    plt.grid(True)
    plt.show()
 
# Data structure: List 
years = [2018, 2019, 2020, 2021, 2022, 2023]
revenue = [50, 75, 90, 100, 87, 105] 
create_line_plot(years, revenue)  
 
# Example 2: Bar Chart 
def create_bar_chart(sales_data):
    if len(sales_data) > 0: 
        products = list(sales_data.keys()) 
        sales = list(sales_data.values())  
        plt.bar(products, sales, color='skyblue')  # Method: plt.bar() to create a bar chart
        plt.title("Sales Performance by Product")  
        plt.xlabel("Product Category")  
        plt.ylabel("Units Sold")  
        plt.show()
    else:
        print("No sales data is available to create the bar chart.")
 
# Data structure: Dictionary
sales_data = {"T-Shirts": 500, "Jeans": 700, "Jackets": 600, "Sneakers": 850}
create_bar_chart(sales_data)  
 
# Example 3: Scatter Plot 
def create_scatter_plot(sales_vs_profit):
    sales = []  
    profit = [] 
 
    for point in sales_vs_profit:  
        sales.append(point[0])  
        profit.append(point[1])  
 
    plt.scatter(sales, profit, color='green')  # Method: plt.scatter() to create a scatter plot
    plt.title("Sales vs Profit Analysis") 
    plt.xlabel("Total Sales (in Units)") 
    plt.ylabel("Profit Earned (in USD)") 
    plt.show()
 
# Data structure: Tuple 
sales_vs_profit_data = [(100, 2400), (200, 3500), (300, 5000), (400, 7500), (500, 12000)]
create_scatter_plot(sales_vs_profit_data) 
