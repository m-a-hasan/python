from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# TODO: 4. Check transaction successful
# TODO: 5. Make coffee

menu = Menu()
# item = MenuItem()
maker = CoffeeMaker()
money = MoneyMachine()

machineOn = True

while machineOn:
    userChoice = input(f"What would you like? ({menu.get_items()}): ")
    if userChoice == "off":
        machineOn = False
        print("Shutting down...")
        break
    elif userChoice == "report":
        maker.report()
        money.report()
    else:
        item = menu.find_drink(userChoice)
        if item is not None:
            if maker.is_resource_sufficient(item):
                if money.make_payment(item.cost):
                    maker.make_coffee(item)
