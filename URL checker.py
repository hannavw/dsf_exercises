# URL checker

import requests
ask_url = input("Please insert an url: ").strip()

r = requests.get(ask_url)
statuscode = r.status_code
#status code = 

if statuscode != 200:
    print("ERROR PANIC")
    

for key, value in r.headers.items():
    print(f'{key}: {value}')

#print(r.text)
text = r.text

index = 0
while index < 10:
    lines = text.splitlines()[index]
    print(lines)
    index = index + 1