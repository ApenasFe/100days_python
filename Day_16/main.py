from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
money = MoneyMachine()
drinks = menu.get_items()

def ask_drink():
    while True:
        user_drink = input(f'Digite o nome de uma das seguintes bebidas: {drinks}')
        drink_search = menu.find_drink(user_drink)
        
        if drink_search == None:
            True
        else:
            return drink_search

def check_resource(drink):
    resource_condition = machine.is_resource_sufficient(drink)

    if resource_condition == True:
        return resource_condition
    else:
        print('Recurso insuficiente')


print('Bem-vindo ao programa')
print('')

while True:
    user_choice = input('Digite "r" para verificar os recursos da máquina ou "c" para fazer um café\n')
    if user_choice == "r":
        machine.report()
    elif user_choice == "c":
        chosen_drink = ask_drink()
        check_resource(chosen_drink)

    else:
        print('Não é uma opção válida')
        True