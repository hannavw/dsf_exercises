import requests
import json
from IPython.display import display, Image

# Ask input from the user.
article = input("Please insert an article name: ").strip().replace(" ","_")
language = input("In what language? en/nl/de " ).strip().lower()

# Complete the url and request it.
url = f'https://{language}.wikipedia.org/api/rest_v1/page/summary/{article}'
r = requests.get(url)

# Check status code and exit it if it's not 200.
if r.status_code != 200:
    exit()

# Load text 
text = r.text 
data = json.loads(text)

# Name variables that are present in the json file and print them.
title = data["title"]
description = data["description"]
extract = data["extract"]
thumbnail = data["thumbnail"]

print(f'\n{language.upper()}')
print(f'Title: {title}')
print(f'Description: {description}')
print(f'Extract: {extract}')
print(url)

# Print image.
url_image = thumbnail["source"]

img = Image(url_image)
display(img)