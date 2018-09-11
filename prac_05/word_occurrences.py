text = input("Text: ")
words = text.split()
word_occurances = {}
for word in words:
    if word in word_occurances:
        word_occurances[word] += 1
    else:
        word_occurances[word] = 1

for word in sorted(word_occurances):
    print("{:<2} - {}".format(word_occurances[word], word))
