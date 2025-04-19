'''Add a number given by the user to the sum provided'''
sum = 100
user_input = input("Please enter a number to add to the previous sum: ")
sum += user_input
print(f'The new sum is: {sum}')
except TypeError as error:
    print("There was an error")
except ValueError:
    print("The user entered some value that was off.")
    continue