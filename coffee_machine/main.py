from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
continue_ordering = True

while continue_ordering:
    order = input(f"What would you like to order? {menu.get_items()} ")
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        continue_ordering = False
    else:
        drink_to_make = menu.find_drink(order)
        if coffee_maker.is_resource_sufficient(drink_to_make):
            if money_machine.make_payment(drink_to_make.cost):
                coffee_maker.make_coffee(drink_to_make)








