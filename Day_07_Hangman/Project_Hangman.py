import random

word_list = ["ardvark", "baboon", "camel"]

word = random.choice(word_list)

guess = input("Guess a letter: ").lower()

for letter in word:
    if(letter == guess):
        print("Right")
    else:
        print("Wrong")