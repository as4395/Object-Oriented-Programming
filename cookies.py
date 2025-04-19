# The script checks if the user has the ingredients necessary to make chocolate chip cookies

ingredients = ("flour", "butter", "sugar", "eggs", "chocolate chips")

user_ingredients = ()

while True:
    ingredient = input("Please enter your ingredients. Once you are done, enter 'stop ").strip().lower()

    if ingredient == 'stop':
        break

    if ingredient in ingredients and ingredient not in user_ingredients:
        user_ingredients += (ingredient, )

if len(user_ingredients) == len(ingredients):
    print("You are ready to start making cookies!")
else:
    print("You are missing some ingredients.")
