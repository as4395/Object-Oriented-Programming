# This script calculates the average of the numbers the user enters until they choose to stop

total = 0
count = 0

while True:
    user_input = input("Please enter as many numbers as you would like. When you are done, enter 'stop'")

    if user_input.lower() == 'stop':
        break
    elif user_input.isdigit():
        number = int(user_input)  
        total += number 
        count += 1  
    else:
        print(f"'{user_input}' is not a valid number.")

if count > 0:
    average = total / count
    print(f'The average of the numbers you entered is: {average}') 
else:
    print("No numbers were entered. The average cannot be calculated.")
