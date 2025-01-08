# 100 Days of code
# Day 15 Project: Higher and Lower game 
# 1/8/2025

MENU = {
    "espresso":{
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

profit = 0 # to track the money inserted inside the coffee machine


def is_resource_sufficient(order_ingredients):
    """Returns True if there is enough resources, False if not."""
    for ingredient in order_ingredients:
        if order_ingredients[ingredient] > resources[ingredient]:
            print(f"Sorry, there is not enough {ingredient}.")
            return False
    return True


def process_coins():
    """Returns the amount of coins inserted."""
    print("Please insert coins.")
    quarters = int(input("How many quarters? ")) * 0.25
    dimes = int(input("How many dimes? ")) * 0.10
    nickels = int(input("How many nickels? ")) * 0.05
    pennies = int(input("How many pennies? ")) * 0.01
    total = quarters + dimes + nickels + pennies
    return total


def is_transaction_successful(coins_inserted, drink_price):
    """Returns True if the money inserted in enough, False if not."""
    if coins_inserted >= drink_price:
        change = round(coins_inserted - drink_price, 2)
        print(f"Here is ${change} in change.") 
        global profit
        profit += drink_price
        return True
    else:
        print(f"Sorry that's not enough money ${coins_inserted}, Money refunded, you need to insert ${drink_price}")
        return False


def make_coffee(drink_name, drink_ingredients):
    """Subtracts the needed ingredients from available resources."""
    for ingredient in drink_ingredients:
        resources[ingredient] -= drink_ingredients[ingredient]
    print(f"Here is your {drink_name} ☕.")


machine_on = True
while machine_on:
    user_choice = input("What would you like? (espresso/latte/cappuccino): ")
    if user_choice == "off":
        machine_on = False
    elif user_choice == "report":
        print(f"Water: {resources['water']}ml.")
        print(f"Milk: {resources['milk']}ml.")
        print(f"Coffee: {resources['coffee']}g.")
        print(f"Money: ${profit}.")
    else:
        drink = MENU[user_choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(user_choice, drink["ingredients"])
                
    
