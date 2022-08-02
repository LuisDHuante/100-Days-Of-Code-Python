import os

title = """
              _____  _____                                     .__    .__               
  ____  _____/ ____\/ ____\____   ____     _____ _____    ____ |  |__ |__| ____   ____  
_/ ___\/  _ \   __\\   __\/ __ \_/ __ \   /     \\__  \ _/ ___\|  |  \|  |/    \_/ __ \ 
\  \__(  <_> )  |   |  | \  ___/\  ___/  |  Y Y  \/ __ \\  \___|   Y  \  |   |  \  ___/ 
 \___  >____/|__|   |__|  \___  >\___  > |__|_|  (____  /\___  >___|  /__|___|  /\___  >
     \/                       \/     \/        \/     \/     \/     \/        \/     \/ 

"""
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0
}


def making_beverage(drink, cost, order_ingredients):

    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            os.system("cls")
            print(f"Sorry there is not enough {item}.")
            sufficient_resources = False
        else: 
            sufficient_resources = True
    

    #Missing: check if resources for {drink} are enough
    while sufficient_resources == True:

        #Asking how many money units the user is going to pay with.
        quarters = float(input("How many quarters?: ")) * 0.25
        dimes = float(input("How many dimes?: ")) * 0.10
        nickles = float(input("How many nickles?: ")) * 0.05
        pennies = float(input("How many pennies?: ")) * 0.01
        total_payment = quarters + dimes + nickles + pennies

        if drink == 'espresso':
            for item in order_ingredients:
                resources[item] -= order_ingredients[item] 

        elif drink == 'latte':
            for item in order_ingredients:
                resources[item] -= order_ingredients[item]
        
        elif drink == 'cappuccino':
            for item in order_ingredients:
                resources[item] -= order_ingredients[item]

        #Missing: add and remove elements from resource values
        if cost > total_payment:
            os.system("cls")
            print("Sorry that's not enough money. Money refunded. ")
            break
        elif cost == total_payment:
            print(f"Here is your {drink}. Enjoy!")
            break
        elif cost < total_payment:
            change = total_payment - cost
            resources["money"] += cost
            os.system("cls")
            print(f"Here is ${round(change, 2)} dollars in change.")
            print(f"Here is your {drink}. Enjoy ☕️!")
            break
        


def coffee_machine():
    #Veryfing order
    while True:
        print(title)
        order = input("What would you like to order? (espresso/latte/cappuccino): ")
        if order == "espresso":
            drink = MENU[order]
            os.system("cls")
            print(title)
            making_beverage(order, 1.5, drink["ingredients"])
        elif order == "latte":
            drink = MENU[order]
            os.system("cls")
            print(title)
            making_beverage(order, 2.5, drink["ingredients"])
        elif order == "cappuccino":
            drink = MENU[order]
            os.system("cls")
            print(title)
            making_beverage(order, 3, drink["ingredients"])
        elif order == "report":
            os.system("cls")
            print(f"Water: {resources['water']}ml")
            print(f"Milk: {resources['milk']}ml")
            print(f"Coffee: {resources['coffee']}g")
            print(f"Money: ${resources['money']}")
        elif order == "off":
            break


if __name__ == "__main__":
    coffee_machine()