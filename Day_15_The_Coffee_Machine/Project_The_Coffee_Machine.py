from Data_Base import resources, MENU
from os import system
from time import sleep

MONEY = 0

def check_resources(drink):
    """Check if the resourses are sufficient to make the drink"""
    for ingredient in MENU[drink]["ingredients"]:
        item = MENU[drink]["ingredients"][ingredient]
        resource = resources[ingredient]
        if(item <= resource):
            resources[ingredient] -= item
        else:
            print(f'Sorry but there is not enought {ingredient}')
            break
        

drink = "start"

while(drink != "end"):
    sleep(3)
    system("cls")
    drink = input("What would you like? (espresso/latte/cappuccino): ").lower()
    if(drink == "report"):
        print(f'Water: {resources["water"]} ml')
        print(f'Milk: {resources["milk"]} ml')
        print(f'Coffee: {resources["coffee"]} ml')
        print(f'Money: ${MONEY}')

    else:
        check_resources(drink)
        print("Passou mesmo assim")