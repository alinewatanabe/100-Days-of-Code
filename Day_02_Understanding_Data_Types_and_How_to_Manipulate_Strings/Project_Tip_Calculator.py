print("Welcome to the tip calculator.")

bill = float(input("What was the total bill? $"))
porcent = float(input("What porcentage tip would you like to give? 10, 12, or 15? "))
people = int(input("How many people to split the bill? "))

tax = (1 + porcent/100)
person_pay = round((bill/people)*tax, 2)
print(f"Each person should pay: ${person_pay}")