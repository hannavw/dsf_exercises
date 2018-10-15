import requests
import json
from IPython.display import display, Image

# Ask input from the user
article = input("Please insert an article name: ").strip().replace(" ","_")
language = input("In what language? en/nl/de " ).strip().lower()

url = f'https://{language}.wikipedia.org/api/rest_v1/page/summary/{article}'
r = requests.get(url)
    
if r.status_code != 200:
    exit()
	
text = r.text 
data = json.loads(text)

#for key, value in r.headers.items():
title = data["title"]
description = data["description"]
extract = data["extract"]
thumbnail = data["thumbnail"]

print(f'\n{language.upper()}')
print(f'Title: {title}')
print(f'Description: {description}')
print(f'Extract: {extract}')
print(url)

url_image = thumbnail["source"]

img = Image(url_image)
display(img)