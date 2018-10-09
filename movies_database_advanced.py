# Import file
import json
with open("movies.json") as f:
	movies = json.load(f)

print("You can filter the database. Please choose an option:") 

# Create a loop and give filter options. A user can filter untill they don't want to anymore.
while True:
    print("1: Filter on duration")  
    print("2: Filter on actor")
    print("3: Director is also an actor")
    print("4: Filter on a genre")
    print("5: Filter on release year")

# Ask the user for input
    option = input("Insert your option: ")
    
# Filter through the database based on the choice of the user.
    if option == "1":
        minutes = int(input("Choose the minimum amount of minutes to filter: "))
        for movie in movies:
            duration = movie["duration"]
            title = movie["title"]
            if duration >= minutes:
                print(f'The movie {title} is {duration} minutes.')
                
    if option == "2":
        actor = input("Choose an actor: ").strip().title()
        for movie in movies:
            actors = movie["actors"]
            title = movie["title"]
            if actor in actors:
                print(f'{actor} played in {title}.')
                
    if option == "3":
        for movie in movies:
            actors = movie["actors"]
            director = movie["director"]
            title = movie["title"]
            if director in actors:
                print(f'{director} is also an actor in the movie {title}')
                
    if option == "4":
        genre = input("Choose a genre: ").strip().lower()
        for movie in movies:
            genres = movie["genres"]
            title= movie["title"]
            if genre in genres:
                print(f'{title} has the genre {genre}')
            
    if option == "5":
        year_input = int(input("Enter a year from which you want to see all the movies: "))
        for movie in movies:
            year = movie["year"]
            title = movie["title"]
            if year == year_input:
                print(f'The movie {title} is from the year {year}.')
                
# Give feedback to the user if he gave wrong input and give an option to try again. 
    if option > "5":
        print("You've chosen a non-existing option.")
    follow_up = input("Do you want to filter the database again? yes/no: ").strip().lower()
    if follow_up == "yes":
        print("Oke! You can filter the database again. Please choose an option:")
    else:
        print("Goodbye!")
        break
        
