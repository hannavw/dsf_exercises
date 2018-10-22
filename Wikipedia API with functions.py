import requests
import json
        
def api_call(title, value):
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{title}"
    req = requests.get(url)
    data = req.json()
    if value == "description":
        print(data["description"])
    elif value == "extract":
        print(data["extract"])
    elif req.status_code != 200:
        exit()
#    return title, value

title = input("Give an article you want to lookup: ").strip()
value = input("Do you want the description or extract?  ").strip().lower()
print(f'Here is the {value} for {title}: ')
data = api_call(title, value)
