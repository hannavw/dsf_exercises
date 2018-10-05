sentence = input("Write a sentence")
lenght = len(sentence)
percent1 = round(len(sentence) / 100 * 25)
percent2 = round(len(sentence) / 100 * 75)
#percent1 = sentence[:percent1]
#percent2 = sentence[percent2:]
print(sentence[percent1:percent2])

#extra
sentence = input("Write a sentence")
sentence = list(sentence.split(" "))
sentence_len = int(len(sentence))
percent1 = int(sentence_len / 100 * 25)
percent2 = int(sentence_len / 100 * 75)
