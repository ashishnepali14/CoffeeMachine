from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()
menu = Menu()
continue_ordering = True

while continue_ordering:
    order = input(f"What would you like to order? {menu.get_items()} ") 
    # I would add report and off here, with some text to make clear what they do. Also the costs!
    if order == "report":
        coffee_maker.report()
        money_machine.report()
    elif order == "off":
        continue_ordering = False
    else:
        drink_to_make = menu.find_drink(order) 
        # unfortunately this assumes a drink will be found, you have an error message if its not
        # but it then crashes the program. You need to handle the case where the drink doesn't exist.
        if coffee_maker.is_resource_sufficient(drink_to_make):
            if money_machine.make_payment(drink_to_make.cost):
                coffee_maker.make_coffee(drink_to_make)
        # these if statements are the right way round (no need to ask for money if you can't make the drink)








