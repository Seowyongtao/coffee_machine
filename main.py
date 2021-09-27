# TODO: 1. data provided

MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "money": 0
}

while not False:

    # TODO: 2. prompt user to ask what they want
    userInput = input("What would you like? (espresso/latte/cappuccino): ")

    # TODO: 3. stop executing the code if the user input "off"
    if userInput == "off":
        break

    # TODO: 4. print report
    elif userInput == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${round(resources['money'],2)}")
        continue

    # TODO: 5. Check whether resource is sufficient
    else:

        coffeeOrdered = MENU[userInput]

        if coffeeOrdered["ingredients"]["water"] >= resources["water"] or coffeeOrdered["ingredients"]["milk"] >= \
                resources["milk"] or coffeeOrdered["ingredients"]["coffee"] >= resources["coffee"]:
            print("Sorry, there is not enough water")
            continue

    # TODO: 6. Process coins
    print("Please insert coins.")

    quarters = input("how many quarters?: ")
    dimes = input("how many dimes?: ")
    nickles = input("how many nickles?: ")
    pennies = input("how many pennies?: ")

    moneyPaid = (0.25 * int(quarters)) + (0.10 * int(dimes)) + (0.05 * int(nickles)) + (0.01 * int(pennies))

    coffeeOrdered = MENU[userInput]

    if moneyPaid < coffeeOrdered["cost"]:
        print("Sorry, that's not enough money. Money refunded")
        continue

    change = moneyPaid - coffeeOrdered["cost"]
    print("Here is $" + str(round(change, 2)) + " in change.\nHere is your " + userInput + ". Enjoy!")

    # TODO : 7. Deduct resources and increase money after making coffee
    resources["water"] -= coffeeOrdered["ingredients"]["water"]
    resources["milk"] -= coffeeOrdered["ingredients"]["milk"]
    resources["coffee"] -= coffeeOrdered["ingredients"]["coffee"]
    resources["money"] += coffeeOrdered["cost"]

