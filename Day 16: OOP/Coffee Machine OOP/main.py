from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

money_machine = MoneyMachine()

ask_user = input('What would you like? (espresso/latte/cappuccino): ')

if ask_user == 'espresso':
    