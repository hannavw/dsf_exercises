forbidden_words = ["sunglasses", "lipstick", "nailpolish", "handbag", "hat"]
good_words = ["🕶","💄","💅","👜","👒"]
new_sentence = []
sentence = input("What do you take with you on your holiday? ").strip().lower()

sentence = sentence.split(" ")

for sentence_word in sentence: #je krijgt: sentence word1 = Ik sentence word2 = vind sentence word3 = Leon
    if sentence_word in forbidden_words:
        index = forbidden_words.index(sentence_word) # Uitkomst is 1
        new_word = good_words[index] # Uitkomst is leon2
        print("New word is: " + new_word)
        new_sentence.append(new_word) #als de if statement klopt, wordt het woord vervangen door het nieuwe woord
    else: 
        new_sentence.append(sentence_word) #als de if statement niet klopt, wordt het woord vervangen door hetzelfde woord

new_sentence = (" ".join(new_sentence)
print(new_sentence)