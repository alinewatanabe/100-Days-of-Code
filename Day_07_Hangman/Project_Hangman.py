import random

word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)
word_length = len(word)

print(f"The answer is: {word}")

display = []
end_of_game = False

for _ in range(word_length):
    display += "_"
print(display)

while (not end_of_game):
    guess = input("Guess a letter: ").lower()
    
    for position in range(word_length):
        letter = word[position]
        if(letter == guess):
            display[position] = letter         
    print(display)
    
    if "_" not in display:
        end_of_game = True
        print("You win!")