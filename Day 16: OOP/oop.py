# from turtle import Turtle, Screen
# import another_module

# print(another_module.another_variable)

# donny = Turtle()
# print(donny)
# donny.shape('turtle')
# donny.color('DarkRed')

# my_screen = Screen()
# print(my_screen.canvheight)
# my_screen.exitonclick()

from prettytable import PrettyTable
table = PrettyTable()
table.add_column('Pokemon Name', ['Squirtle', 'Charmander', 'Eevee'])
table.add_column('Type', ['Water', 'Fire', 'Normal'])

table.align = 'l'

print(table)