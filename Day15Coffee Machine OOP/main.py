from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu_item = MenuItem
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_on = True
while is_on:

    print("--- Coffee Machine ---")
    choice = input("Which coffee would you like? (espresso/latte/cappuccino): ")  .lower()
    if choice == "report":
        coffee_maker.report()
        money_machine.report()
    elif choice == "off":
        is_on = False
    else:
        print("Please enter a valid option.\n")