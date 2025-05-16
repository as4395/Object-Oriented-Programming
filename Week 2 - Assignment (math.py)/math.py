# Prompt the user to enter the first integer, followed by the second integer
num_1 = int(input("Enter the first integer: "))
num_2 = int(input("Enter the second integer: "))

# Calculate the sum of two integers
sum_result = num_1 + num_2
# Calculate the difference (first integer minus the second integer)
difference_result = num_1 - num_2
# Calculate the product (first integer multiplied by the second integer)
product_result = num_1 * num_2
# Calculate the quotient (first integer divided by the second integer) and handle a division by zero error
quotient_result = num_1 / num_2 if num_2 != 0 else "Undefined (division by zero)"
# Calculate the remainder when the first integer is divided by the second integer and handle a division by zero error
remainder_result = num_1 % num_2 if num_2 != 0 else "Undefined (division by zero)"
# Calculate the first number raised to the power of the second number
exponent_result = num_1 ** num_2 

# Print the results of the 6 arithmetic operations
print("The sum of the two integers is: " + str(sum_result))
print("The difference of the two integers is: " + str(difference_result))
print("The product of the two integers is: " + str(product_result))
print("The quotient of the two integers is: " + str(quotient_result))
print("The remainder of the two integers is: " + str(remainder_result))
print("The first number raised to the second number is: " + str(exponent_result))