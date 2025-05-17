import random

# This code generates random Rutgers email addresses based on the predefined list of full names
full_names = (["Alex Johnson", "Samantha Lee", "Juan Rodriguez", "Aaliyah Patel", "Daniel Kim", "Fatima Ali", "Adam Smith"])

rutgers_emails = []

for name in full_names:
    first_name, last_name = name.split()
    random_number = random.randint(100, 999)
    email = f"{first_name[0].lower()}{last_name[0].lower()}{random_number}@rutgers.edu"
    rutgers_emails.append(email)

print(f"Given the list of names, the email addresses associated with these names are:\n{rutgers_emails}") 
