import re
import json
import os
import openai
import webbrowser


def get_minutes(mseconds):
    return mseconds / 60000000.0


def read_recipe(file):
    y = json.loads(file.read())

    for x in range(4):
        print('')
    print(y['name'])
    print(f'Serves: {y["servings"]}')
    print('------')
    if 'cookTime' in y:
        print(f'Cooking time: {get_minutes(y["cookTime"])}')
    if 'prepTime' in y:
        print(f'Prep time: {get_minutes(y["prepTime"])}')
    print('------')
    print('Ingredients')
    for ingredient in y['ingredients']:
        print(f'-- {ingredient["name"]}')
    print('------')
    print('Steps')
    index = 0
    for step in y['instructions']:
        index += 1
        print(f'{index}) {step["text"]}')
    for x in range(4):
        print('')


def parse_ingredient(ingredient):
    match = re.search(
        r'\b(?:\d+\.?\d*|\d*\.?\d+)\s*[a-zA-Z]*\s*([a-zA-Z\- ]+)',
        ingredient)
    if match:
        return match.group(1).strip()
    return None


def gather_ingredients(files):
    ingredients = []

    for recipe in files:
        with open(recipe, 'r') as file:
            y = json.loads(file.read())

            for ingredient in y['ingredients']:
                ingredients.append(ingredient['name'])

    if 'OPENAI_API' in os.environ:
        openai.api_key = os.getenv('OPENAI_API')
    else:
        print('API key not found')
        return ingredients

    outingredients = ''

    for ingredient in ingredients:
        outingredients = outingredients + ingredient + '\n'

    prompt = f'''
        Ingredients:
        {outingredients}

        Tasks:
        1. Merge like-items and convert measurements.
        2. Recommend substitutes for Colorado Springs, CO availability
        3. Format as:
            **CATEGORY**
            [INGREDIENT]: [QUANTITY]
    '''

    messages = [
        {"role": "system", "content": "You are a professional grocery shopper, making the most efficient, time-saving lists in the whole world. Remain brief and highly-efficient."},
        {"role": "user", "content": prompt}
    ]

    response = openai.ChatCompletion.create(
            model='gpt-4',
            messages=messages,
            temperature=0.5,
            max_tokens=500
        )

    print(response.choices[0].message.content)

    return response.choices[0].messages.content.split('\n')
#    response = openai.ChatCompletion.create(
#            model="gpt-3.5-turbo",
#            messages=[
#                {"role": "system", "content": "You are a professional chef and full-time grocery shopping pro. Answer all questions professionally, and truthfully. Do not break character."},
#                {"role": "user", "content": "I will provide you a list of ingredients for my upcoming meals, please condense the list (combine like-ingredients), please convert all measurements into an easily-shoppable measurement ('g' or grams in the US, or equivalent for the food item). Ensure the following format for your output of condensed ingredients: {QUANTITY} - {INGREDIENT}, replacing the all-capital placeholders with their appropriate value. Do you understand?"},
#                {"role": "assistant", "content": "I understand. I will combine ingredients that share the same name, and convert all measurements into a quote-'easily-shoppable' format for quick and efficient grocery shopping, while maintaining a {qty} - {ingredient} format at all times."},
#                {"role": "user", "content": f"{outingredients}"}
#            ])
#
#    print(response.choices[0].message.content)
#
#    response = openai.ChatCompletion.create(
#            model="gpt-3.5-turbo",
#            messages=[
#                {"role": "system", "content": "You are a professional chef and full-time grocery shopping pro. Answer all questions professionally, and truthfully. Do not break character."},
#                {"role": "user", "content": "I will provide you a list of ingredients for my upcoming meals, please condense the list (combine like-ingredients), please convert all measurements into an easily-shoppable measurement ('g' or grams in the US, or equivalent for the food item). Ensure the following format for your output of condensed ingredients: {QUANTITY} - {INGREDIENT}, replacing the all-capital placeholders with their appropriate value. Do you understand?"},
#                {"role": "assistant", "content": "I understand. I will combine ingredients that share the same name, and convert all measurements into a quote-'easily-shoppable' format for quick and efficient grocery shopping, while maintaining a {qty} - {ingredient} format at all times."},
#                {"role": "user", "content": f"{outingredients}"},
#                {"role": "assistant", "content": response.choices[0].message.content},
#                {"role": "user", "content": "Please re-review your message and confirm you've done a good job. All similar ingredients should only take up one line, with their values combined. Have you done that?"}
#            ])

def open_card(files):
    for recipe in files:
        with open(recipe, 'r') as file:
            y = json.loads(file.read())

            url = y['sourceUrl']

            webbrowser.open(f'https://www.justtherecipe.com/?url={url}')



if __name__ == '__main__':
    print('')
    print('Select an option: ')
    print('1) Select recipes for shopping')
    print('2) Output recipe to console')
    print('3) Open recipe card')

    choice = input()
    allrecipes = []

    for file in os.listdir(os.path.expanduser('~/Recipes/')):
        if file.endswith('.recipe'):
            allrecipes.append(file)

    if int(choice) == 1:
        recipes = []
        print('')
        for file in allrecipes:
            print(f'{allrecipes.index(file) + 1}) {file}')
        print('')
        print('Input comma-separated index of the recipes')
        choice = input()
        for val in choice.split(','):
            recipe = allrecipes[int(val) - 1]
            recipes.append(os.path.expanduser(f'~/Recipes/{recipe}'))
        results = gather_ingredients(recipes)
        with open(os.path.expanduser(f'~/Recipes/Shopping.md'), 'w+') as file:
            for result in results:
                file.write(f'- [ ] {result}\n')
    elif int(choice) == 2:
        print('')
        for file in allrecipes:
            print(f'{allrecipes.index(file) + 1}) {file}')
        print('')
        print('Input the file index')
        index = int(input())
        recipe = allrecipes[index - 1]
        file = open(os.path.expanduser(f'~/Recipes/{recipe}'))
        read_recipe(file)
    elif int(choice) == 3:
        recipes = []
        print('')
        for file in allrecipes:
            print(f'{allrecipes.index(file) + 1}) {file}')
        print('')
        print('Input comma-separated index of the recipes')
        choice = input()
        for val in choice.split(','):
            recipe = allrecipes[int(val) - 1]
            recipes.append(os.path.expanduser(f'~/Recipes/{recipe}'))
        open_card(recipes)
