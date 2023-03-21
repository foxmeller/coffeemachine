from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

is_on = True
money_machine = MoneyMachine()
coffee_maker = CoffeeMaker()
menu = Menu()
# menu_item = MenuItem().name

money_machine.report()
coffee_maker.report()


# print(menu.get_items())
# #
# # cash = money_machine.process_coins()
# # print(cash)
# print(money_machine.make_payment(3))

# print(menu_item)
# coffee_maker.is_resource_sufficient("latte")

print(menu.find_drink("latte"))
latte = menu.find_drink("latte")
print(coffee_maker.is_resource_sufficient(latte))
print(latte.name)

while is_on:
    choice = input(f"What would you like? {menu.get_items()}: ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        money_machine.report()
        coffee_maker.report()
    else:
        drink= menu.find_drink(choice)
        if coffee_maker.is_resource_sufficient(drink):
            payment = money_machine.make_payment(drink.cost)
            if payment :
                coffee_maker.make_coffee(drink)
                # make_coffee(choice, drink["ingredients"])