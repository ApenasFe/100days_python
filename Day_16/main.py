from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
machine = CoffeeMaker()
transaction = MoneyMachine()
drinks = menu.get_items()

def ask_drink():
    while True:
        user_drink = input(f'Digite o nome de uma das seguintes bebidas: {drinks}\n')
        drink_search = menu.find_drink(user_drink)
        
        if drink_search == None:
            True
        else:
            return drink_search

def check_resource(drink):
    verified_resource = machine.is_resource_sufficient(drink)

    if verified_resource == True:
        return verified_resource
    else:
        print('Recurso insuficiente')
        exit_continue()

def transaction_process(drink, resource):
    if resource == True:
        return transaction.make_payment(drink)
    else:
        print('Perdão, algo deu errado na verificação de recursos.')
        exit_continue()

def coffee_order(drink, condition):
    if condition == True:
        machine.make_coffee(drink)
    else:
        exit_continue()

def exit_continue():
    while True:
        user_option = input('Digite "c" para continuar utilizando a máquina ou "e" para sair\n')
        if user_option == "c":
            coffee_machine()
        elif user_option == "e":
            print('Obrigado por utilizar o programa!')
            print('Desenvolvido por Felipe :^)')
            exit()

print('Bem-vindo ao programa')
print('')

def coffee_machine():
    while True:
        user_choice = input('Digite "r" para verificar os recursos da máquina, "p" para verificar quanto a máquina já faturou ou "c" para fazer um café\n')
        if user_choice == "r":
            machine.report()
        elif user_choice == "c":
            chosen_drink = ask_drink()
            resource_condition = check_resource(chosen_drink)
            transaction_condition = transaction_process(chosen_drink.cost, resource_condition)
            coffee_order(chosen_drink, transaction_condition)
            exit_continue()
        elif user_choice == "p":
            transaction.report()
        else:
            print('Não é uma opção válida')
            True

coffee_machine()