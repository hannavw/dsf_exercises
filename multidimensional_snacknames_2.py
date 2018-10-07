# Friends in list and empty list for snacks
friends = [
    ["Marleen"],
    ["Femke"],
    ["Nienke"]
]

# Set index to 0, ask fot input and append that to the list.
index = 0                                           
for friend in friends:
    friend = friends[index][0]
    snack = input(friend + ", what's your favourite snack? ")
    friends[index].append(snack)
    lenght = len(friend)

# Print feedback and add 1 to index
    print(str(friends[index][0]) + " , you like " + str(friends[index][1]) + " and you're name is " + str(lenght) + " letters long.")
    index = index + 1