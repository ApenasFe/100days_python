#Menu da cafeteira
menu = {
    "Espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "Latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "Cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3,
    },
}

#Recursos da maquina
resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

#Escreva o teste logo abaixo
def ask_user():
    choice_condition = True
    while choice_condition:
        user_choice = input('Digite o nome do café que você deseja: Espresso, Latte ou Cappuccino\n').title()

        for key in menu:
            if user_choice == key:
                choice_condition = False
    return user_choice

user_decision = ask_user()

def check_resource(coffee_ingredients, machine_resources):
    for ingredient in coffee_ingredients and machine_resources:
        coffee_value = coffee_ingredients[ingredient]
        machine_value = machine_resources[ingredient]

        if coffee_value <= machine_value:
            return True
        else:
            return False

def subtract_resource(coffee_ingredients):
    for ingredient in coffee_ingredients:
        ingredient_value = coffee_ingredients[ingredient]
        resources[ingredient] -= ingredient_value
        
check_condition = check_resource(menu[user_decision]["ingredients"], resources)


def make_coffe():
    if check_condition == True:
        subtract_resource(menu[user_decision]["ingredients"])
        print(f'Seu café {user_decision} está pronto!')
    else:
        print('Recurso insuficiente')

make_coffe()
