import random

word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)
print(f"The answer is: {word}")

display = []
list = []

print(len(word)*"_")

guess = input("\nGuess a letter: ").lower()

for letter in word:
    if(letter == guess):
        list.append(guess)
    else:
        list.append("_")
           

print(list)