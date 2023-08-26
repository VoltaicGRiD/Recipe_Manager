import requests
import argparse
import os
import json


def download(url):
    response = requests.get(f'https://www.justtherecipe.com/extractRecipeAtUrl?url={url}')
    return response.text


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Download the HTML from "JustTheRecipe.com"')
    parser.add_argument('url', help=('Link to the Recipe'))
    parser.add_argument('title', help=('Title of the Recipe'))
    args = parser.parse_args()
    url = args.url
    title = args.title.replace(" ", "_")

    content = str(download(url))

    y = json.loads(content)
    path = os.path.expanduser(f'~/Recipes/{y["name"]}')

    file = open(f'{path}.recipe', 'w+')
    file.write(content)
    file.close()
