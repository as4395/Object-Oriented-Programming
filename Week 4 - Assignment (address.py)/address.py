# Asks the user for address details and handles empty strings

# First name
first_name = input("What is your first name? ").title()
if not first_name:
    print("First name cannot be empty. Please try again.")
    first_name = input("What is your first name? ").title()
    if not first_name:
        exit(0)

# Last name
last_name = input("What is your last name? ").title()
if not last_name:
    print("Last name cannot be empty. Please try again.")
    last_name = input("What is your last name? ").title()
    if not last_name:
        exit(0)

# Street address
street_address = input("What is your street address? ").title()
if not street_address:
    print("Street address cannot be empty. Please try again.")
    street_address = input("What is your street address? ").title()
    if not street_address:
        exit(0)

# City
city = input("What is your city? ").title()
if not city:
    print("City cannot be empty. Please try again.")
    city = input("What is your city? ").title()
    if not city:
        exit(0)

# State
state = input("What is your state? ").upper()
if not state:
    print("State cannot be empty. Please try again.")
    state = input("What is your state? ").upper()
    if not state:
        exit(0)

# Zip/postal code
zip_code = input("What is your zipcode? ")
if not zip_code:
    print("Zip code cannot be empty. Please try again.")
    zip_code = input("What is your zip code? ")
    if not zip_code:
        exit(0)
            
is_us = input("\nIs the address in the United States? (yes/no): ").lower()

if is_us == "yes":
    # U.S. postal codes must be five digits 
    if len(zip_code) != 5 or not zip_code.isdigit():
        print("Invalid U.S. zip code format. Please enter exactly 5 digits.")
        zip_code = input("What is your zip code? ")
        if not len(zip_code) != 5 or not zip_code.isdigit():
            exit(0)
else:
    # Checks for international postal codes 
    if len(zip_code) < 3 or len(zip_code) > 10:
        print("Invalid postal code. Please enter a valid international postal code.")
        zip_code = input("What is your zip/postal code? ")
        if len(zip_code) < 3 or len(zip_code) > 10:
            exit(0) 

# Prints the structured mailing address
print("\nYour mailing address should be structured as:")
print(f"{first_name} {last_name}")
print(f"{street_address}")
print(f"{city}, {state} {zip_code}")
