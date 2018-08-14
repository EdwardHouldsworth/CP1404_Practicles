"""
CP1404/CP5632 - Practical
Random word generator - based on format of words

Another way to get just consonants would be to use string.ascii_lowercase
(all letters) and remove the vowels.
"""
import random

VOWELS = "aeiou"
CONSONANTS = "bcdfghjklmnpqrstvwxyz"

word_format = str(input("Enter # (consanants) and * (vowels): "))

for x in range(0, 4):
    word = ""
    for kind in word_format:
        if kind == "#":
            word += random.choice(CONSONANTS)
        elif kind == '*':
            word += random.choice(VOWELS)
        else:
            word += kind

    print(word)
