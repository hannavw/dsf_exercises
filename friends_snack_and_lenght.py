# Put my friends in a list
friends = ["Marleen", "Femke", "Nienke"]
snacks = []

# Ask each friend for snack and add snack to a list
index = 0
for friend in friends:
    snack = input(friend + ", What's your favourite snack? ")
    snacks.append(snack)
    index = index + 1
    
# Loop through friends and place a snack from the snack-list after each friend. 
index = 0
for friend in friends:
    length = len(friends[index])
    snack = snacks[index]
    print(friend + ", you're favourite snack is: " + snack + ", and you're name has " + str(length) + " characters.")
    index = index + 1