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


def user_choice():
    return input("What would you like? (espresso/latte/cappuccino): ")


def show_report():
    print("Water: " + str(resources["water"]) + "ml")
    print("Milk: " + str(resources["milk"]) + "ml")
    print("Coffee: " + str(resources["coffee"]) + "g")
    print("Money: $" + str(money))


def check_resources(coffee):
    if MENU[coffee]["ingredients"]["water"] > resources["water"]:
        return "water"
    if "milk" in MENU[coffee]["ingredients"]:
        if MENU[coffee]["ingredients"]["milk"] > resources["milk"]:
            return "milk"
    if MENU[coffee]["ingredients"]["coffee"] > resources["coffee"]:
        return "coffee"


def process_coin(coffee):
    print("Please insert coins.")

    quarters = int(input("How many quarters?: "))
    dimes = int(input("How many dimes?: "))
    nickel = int(input("How many nickel?: "))
    pennies = int(input("How many pennies?: "))
    total = (quarters * 0.25) + (dimes * 0.1) + (nickel * 0.05) + (pennies * 0.01)

    return round(total - MENU[coffee]["cost"], 2)


def complete_transaction(flavour, change):
    global money
    money = money + MENU[flavour]["cost"]
    resources["water"] = resources["water"] - MENU[flavour]["ingredients"]["water"]
    if "milk" in MENU[flavour]["ingredients"]:
        resources["milk"] = resources["milk"] - MENU[flavour]["ingredients"]["milk"]
    resources["coffee"] = resources["coffee"] - MENU[flavour]["ingredients"]["coffee"]

    if change > 0:
        print("Here is $" + str(change) + " in change.")

    print("Here is your " + flavour + ". Enjoy!")


if __name__ == '__main__':
    opt = user_choice()
    while True:
        if opt == "off":
            print("shutting down...")
            break

        elif opt == "report":
            show_report()
            opt = user_choice()

        elif opt == "espresso" or opt == "latte" or opt == "cappuccino":
            shortage = check_resources(opt)
            if shortage == "water" or shortage == "milk" or shortage == "coffee":
                print("Sorry there is not enough " + shortage + ".")
            else:
                coins = process_coin(opt)
                if coins < 0:
                    print("Sorry that's not enough money. Money refunded.")
                else:
                    complete_transaction(opt, coins)

            opt = user_choice()

        else:
            opt = user_choice()
