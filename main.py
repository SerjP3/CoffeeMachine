from itertools import filterfalse

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

money = 0

def check_resources(drink):
    ingredients = MENU[drink]["ingredients"]
    for item in ingredients:
        if ingredients[item] > resources.get(item, 0):
            print(f"Sorry! There is not enough {item}")
            return False
    return True

def make_drink(drink):
    global money
    for item in MENU[drink]["ingredients"]:
        resources[item] -= MENU[drink]["ingredients"][item]
    money += MENU[drink]["cost"]
    print(f"Here is your {drink}. Enjoy!")

def print_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money:.2f}")

def process_coins():
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickels + pennies

    return total

while True:
    choice = input("What would you like? (espresso/latte/cappuccino) ").lower()

    if choice == "off":
        print("The coffee machine is off. GoodBye!")
        break
    elif choice == "report":
        print_report()
    elif choice in MENU:
        if check_resources(choice):
            print(f"Insert coins: ${MENU[choice]["cost"]}")
            payment = process_coins()
            if payment >= MENU[choice]["cost"]:
                change = payment - MENU[choice]["cost"]
                if change > 0:
                    print(f"Here is your change: ${change:.2f}")
                make_drink(choice)
            else:
                print("Sorry, not enough money!")
    else:
        print("Invalid input!")