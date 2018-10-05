#open files
f = open("paintings.csv")
newfile = open("painting2.txt", "w")
for line in f:
	row = line.strip().split(",")
	painting = row[0]
	painter = row[1]
	price = row[2]
	newfile.write(painting + " is a painting by " + painter + " and was sold for " + str(price) + " million dollars." + "\n")

f.close()

f = open("paintings.csv")
newfile = open("painting2.txt", "a")

extra_painting = input("What is the name of the painting? ")
extra_painter = input("Who painted the painting? ")
extra_price = input("How many millions is the painting worth? ")
extra_price = str(float(extra_price) * 100000).replace(".", "")
newfile.write(extra_painting + " is a painting by " + extra_painter + " and was sold for " + str(extra_price) + " million dollars." + "\n")
	
f.close()
newfile.close()