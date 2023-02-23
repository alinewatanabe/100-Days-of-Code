from Art_Project import logo
from os import system
import random

def random_cards(lista):
    card = random.choice(list(cards.keys()))
    lista.append(card)

def keys_to_values(dictionary,old_list, new_list):
    for symbol in old_list:
        new_list.append(dictionary[symbol])

def list_sum(lista):
    S = 0
    for number in lista:
        S += number
         
    

system("cls")
cards = {}
user_list = []
user_values_list = []
comp_list = []

print(logo)

for number in range(1,11):
    cards[number] = number

cards['J'] = 10
cards['Q'] = 10
cards['K'] = 10
cards['A'] = [1, 11]

random_cards(user_list)
random_cards(user_list)

keys_to_values(cards, user_list, user_values_list)

user_score = list_sum(user_values_list)

print(f"Your cards : {user_list}, current score: {user_score}")
