import random

stages = ['''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========
''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========
''', '''
  +---+
  |   |
      |
      |
      |
      |
=========
''']

word_list = ["ardvark", "baboon", "camel"]
word = random.choice(word_list)
word_length = len(word)

print(f"The answer is: {word}")

display = []
end_of_game = False
lives = 6

for _ in range(word_length):
    display += "_"

while (not end_of_game):
    print(stages[lives])
    guess = input("\nGuess a letter: ").lower()
    
    for position in range(word_length):
        letter = word[position]
        if(letter == guess):
            display[position] = letter
            
    print(f"{' '.join(display)}")
    
    if "_" not in display:
        end_of_game = True
        print("You win!")

    if guess not in word:
        lives -= 1

    if lives < 0:
        end_of_game = True
        print("You lose")