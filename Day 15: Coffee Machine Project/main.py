from tkinter import Menu


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

question = input('What would you like? (espresso/latte/cappuccino): ')

if question == 'report':
    print(resources)
elif question == 'espresso' or question == 'latte' or question == 'cappuccino':
    print('Please insert coins.')
    input2 = input('How many quarters? ')