'https://api.edamam.com/search?q={}&app_id=e93cc8a7&app_key=6379bab9a3568442befcdce68756635c'
import requests


def recipe_search(ingredient, maxCalories, healthLabel):
    # Register to get an APP ID and key https://developer.edamam.com/
    app_id = 'e93cc8a7'
    app_key = '6379bab9a3568442befcdce68756635c'
    result = requests.get('https://api.edamam.com/search?q={}&calories={}&health={}&app_id={}&app_key={}'.format(ingredient, maxCalories, healthLabel, app_id, app_key))
    data = result.json()
    print(data)
    return data['hits']


def add_recipe(recipe, add_to_file):
    if add_to_file == "n":
        print('How about this recipe?')
    else:
        new_recipe = recipe['label'] + '\n' + recipe['uri']
        with open('recipes.txt', 'r') as text_file:
            recipe_list = text_file.read()
            recipe_list = recipe_list + new_recipe + '\n'
        with open('recipes.txt', 'w+') as text_file:
            text_file.write(recipe_list)


def run():
    ingredient = input('Enter an ingredient: ')
    maxCalories = input('Enter a calorie limit: ')
    healthLabel = input('Enter a health label: ')
    results = recipe_search(ingredient, maxCalories, healthLabel)
    for result in results:
        recipe = result['recipe']
        print(recipe['label'] + '\n' + recipe['uri'])
        add_to_file = input("Would you like to add this recipe to your list? y/n ")
        add_recipe(recipe, add_to_file)
        if add_to_file == 'y':
            print("This recipe has been added to your list.")
            break


run()