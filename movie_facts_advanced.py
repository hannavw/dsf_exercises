# Movie facts
movie_facts = {
        "Title" : "Because I said so",
        "Release_year" : 2007,
        "Duration" : 102,
        "Director" : "Michael Lehmann"
        }

# Add new item in the dictionary. You can also just put it in the dictonary. 
movie_facts["Actors"] = ["Diane Keaton", "Mandy Moore", "Gabriel Macht"]

# Create a for loop and print different things for duration and actors.

for key,value in movie_facts.items():
    if key == "Duration":
        print(f'{key}: {value} minutes')
    elif key == "Actors":
        print(f'{key}: {", ".join(value)}')
    else:
        print(f'{key}: {value}')