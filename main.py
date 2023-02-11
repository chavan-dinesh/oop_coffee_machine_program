from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
# menu_items = MenuItem()
menu = Menu()
is_on = True

while is_on:
    options = menu.get_items()
    choice = input(f"Choose drink ? {options} : ")
    if choice == "off":
        print("Switching OFF Coffee Machine.")
        is_on = False
    elif choice == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(choice)
        can_make = coffee_maker.is_resource_sufficient(drink)
        if can_make:
            can_pay = money_machine.make_payment(drink.cost)
            if can_pay:
                coffee_maker.make_coffee(drink)
