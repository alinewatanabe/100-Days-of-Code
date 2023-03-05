def resources():
    print(f"Water: {water}ml")
    print(f"Milk: {milk}ml")
    print(f"Coffee: {coffee}g")
    
def verification(drink, water, coffee, milk):
    if (drink == 'espresso'):
        check_w = water - 50 > 0
        check_c = coffee - 18 > 0
    return (check_w and check_c)

def pay(price):
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.1
    nickles = int(input("How many nickles? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickles + pennies
    if(total > price):
        print(f"Here is ${total - price} in change")
    elif(total < price):
        print(f"Sorry that's not enought money. Money refunded")
    else:
        print("Thanks! Enjoy your drink")
        
water = 300
milk = 200
coffee = 100

espresso_price = 1.5
latte_price = 2.5
cappuccino_price = 3

drink = input("What would you like? (espresso/latte/cappuccino): ").lower()

if(drink == "report"):
    resources()

if(drink == 'espresso'):
    check = verification(drink, water, coffee, milk)
    if (check == 'True'):
        pay(espresso_price)
    else:
        print("Resources ")
