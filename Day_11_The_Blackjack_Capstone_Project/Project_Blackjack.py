import random

def add_card(view_list, cards, user_list, symbol_cards):
    value_random = random.choice(cards)
    position = cards.index(value_random)
    user_list.append(value_random)
    view_list.append(symbol_cards[position])

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
symbol_cards = ["A", 2, 3, 4, 5, 6, 7, 8, 9, 10, "J", "Q", "K"]
user_list = []
view_user_list = []
computer_list = []
view_comp_list = []

# Add Initial User Cards
add_card(view_user_list, cards, user_list, symbol_cards)
add_card(view_user_list, cards, user_list, symbol_cards)

# Add Initial Computer Cards
add_card(view_comp_list, cards, computer_list, symbol_cards)
add_card(view_comp_list, cards, computer_list, symbol_cards)

score = 0
for number in user_list:
    score += number
    
print(f"Your cards: {view_user_list}, current score: {score}")