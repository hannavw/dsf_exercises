# Friends in list and empty list for snacks
friends = [
    ["Marleen"],
    ["Femke"],
    ["Nienke"]
]

index = 0                                           
for friend in friends:
    snack = input(friends[index]) + ", What's your favourite snack? ")
    friend.append(snack)
#    friends_snacks = [friends[index], snacks[index]]
    lenght = len(friend)
    print(friends[index] + "you're name is " + str(lenght) + " letters long and you like a " + snacks[index])
    index = index + 1