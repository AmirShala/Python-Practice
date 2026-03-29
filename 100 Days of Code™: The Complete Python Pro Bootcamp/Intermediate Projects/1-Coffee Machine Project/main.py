"""
Coffee Machine Program

Overview:
---------
Simulates a coffee machine that serves espresso, latte, and cappuccino.
The user selects a drink, inserts coins, and the machine checks resources,
processes payment, and serves the drink if possible.

Functions:
----------
is_resource_sufficient(order_ingredients: dict) -> bool
    Checks if there are enough resources to make the selected drink.
    Prints a message and returns False if any ingredient is insufficient.

process_coins() -> float
    Prompts the user to insert coins and calculates the total amount.

is_transaction_successful(money_received: float, drink_cost: float) -> bool
    Returns True if enough money was inserted.
    Updates profit and returns change if applicable.

make_coffee(drink_name: str, order_ingredients: dict) -> None
    Deducts ingredients from resources and serves the drink.

Main Flow:
----------
- Ask user for input (drink/report/off)
- If "report": display current resources and profit
- If drink selected:
    - Check resources
    - Process payment
    - If payment successful → make coffee

Variables:
----------
MENU (dict): Contains drink recipes and costs
resources (dict): Tracks available ingredients
profit (float): Tracks total earnings
is_on (bool): Controls the machine loop

Notes:
------
- Uses global variable 'profit' for tracking money
- Resources are updated after each successful order
- Basic input handling (no validation for invalid drink names)
"""


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

profit = 0
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(order_ingredients):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}.")
            return False
    return True


def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    total = int(input("how many quarters?: ")) * 0.25
    total += int(input("how many dimes?: ")) * 0.1
    total += int(input("how many nickles?: ")) * 0.05
    total += int(input("how many pennies?: ")) * 0.01
    return total


def is_transaction_successful(money_received, drink_cost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if money_received >= drink_cost:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True
    else:
        print("Sorry that's not enough money. Money refunded.")
        return False


def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    else:
        drink = MENU[choice]
        if is_resource_sufficient(drink["ingredients"]):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(choice, drink["ingredients"])








