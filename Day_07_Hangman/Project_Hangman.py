import random

word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)
print(f"The answer is: {word}")

list = []
list_conf = []

print(len(word)*"_")

guess = input("\nGuess a letter: ").lower()

for letter in word:
    if(letter == guess):
        ans = "Right"
        print("Right")
    else:
        ans = "Wrong"
        print("Wrong")
    list.append(ans)

for answer in list:
    if(answer == "Wrong"):
        list_conf.append("_")
    else:
        list_conf.append(guess)

print(list_conf)