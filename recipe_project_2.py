import requests


def recipe_search1():  # with health filter
    app_id = 'c17ca92e'
    app_key = '65b289f0f7e414fbc4100547498596ff'
    ingredient = input('What ingredient would you like to search for? ')
    health = input('What is the dietary requirement? Eg vegan, vegetarian, peanut-free ')
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}&health={}'.format(ingredient, app_id, app_key, health))

    data = result.json()
    return data['hits']


def recipe_search2():  # without health filter
    app_id = 'c17ca92e'
    app_key = '65b289f0f7e414fbc4100547498596ff'
    ingredient = input('What ingredient would you like to search for? ')
    result = requests.get('https://api.edamam.com/search?q={}&app_id={}&app_key={}'.format(ingredient, app_id, app_key))

    data = result.json()
    return data['hits']


def run():
    dietary_requirement = input('Do you have any dietary requirements? y/n ')
    calorie_count = input('Would you like to set a calorie limit? y/n ')

    if calorie_count == 'y' and dietary_requirement == 'y':
        max_calories = input('What is the maximum number of calories for the dish? ')
        result = recipe_search1()

        for results in result:

            recipe = results['recipe']

            if int(recipe["calories"]) < int(max_calories):

                print(recipe['label'])  # print recipe name
                print(recipe['uri'])  # print recipe link
                print(recipe['mealType'])  # print the type of meal
                print(recipe['ingredientLines'])  # print ingredients list
                print('Calories:', int(recipe['calories']))  # print calories as integers not float
                print(recipe['healthLabels'])  # print health labels
                print()

                with open('recipes.txt', 'a+') as recipes_file:
                    recipes_file.write(recipe['label'] + '\n')
                    recipes_file.write(recipe['uri'] + '\n')

    elif calorie_count == 'n' and dietary_requirement == 'y':
        result = recipe_search1()

        for results in result:

            recipe = results['recipe']

            print(recipe['label'])  # print recipe name
            print(recipe['uri'])  # print recipe link
            print(recipe['mealType'])  # print the type of meal
            print(recipe['ingredientLines'])  # print ingredients list
            print('Calories:', int(recipe['calories']))  # print calories as integers not float
            print(recipe['healthLabels'])
            print()

            recipes_data = recipe['label'] + '\n' + recipe['uri'] + '\n'

            with open('recipes.txt', 'a+') as recipes_file:
                recipes_file.write(recipes_data)

    elif calorie_count == 'y' and dietary_requirement == 'n':
        max_calories = input('What is the maximum number of calories for the dish? ')
        result = recipe_search2()

        for results in result:

            recipe = results['recipe']

            if int(recipe["calories"]) < int(max_calories):
                print(recipe['label'])  # print recipe name
                print(recipe['uri'])  # print recipe link
                print(recipe['mealType'])  # print the type of meal
                print(recipe['ingredientLines'])  # print ingredients list
                print('Calories:', int(recipe['calories']))  # print calories as integers not float
                print()

                with open('recipes.txt', 'a+') as recipes_file:
                    recipes_file.write(recipe['label'] + '\n')
                    recipes_file.write(recipe['uri'] + '\n')

    else:
        result = recipe_search2()

        for results in result:

            recipe = results['recipe']

            print(recipe['label'])  # print recipe name
            print(recipe['uri'])  # print recipe link
            print(recipe['mealType'])  # print the type of meal
            print(recipe['ingredientLines'])  # print ingredients list
            print('Calories:', int(recipe['calories']))  # print calories as integers not float
            print()

            with open('recipes.txt', 'a+') as recipes_file:
                recipes_file.write(recipe['label'] + '\n')
                recipes_file.write(recipe['uri'] + '\n')


run()
