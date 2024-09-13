#Biblioteca
from ascii_art import art
import os
#Função para limpar interface do terminal de qualquer OS
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Menu da maquina
menu = {
    "Espresso": {
        "ingredients": {
            "água": 50,
            "café": 18,
        },
        "cost": 1.5,
    },
    "Latte": {
        "ingredients": {
            "água": 200,
            "leite": 150,
            "café": 24,
        },
        "cost": 2.5,
    },
    "Cappuccino": {
        "ingredients": {
            "água": 250,
            "leite": 100,
            "café": 24,
        },
        "cost": 3,
    },
}

#Recursos da maquina
resources = {
    "água": 300,
    "leite": 200,
    "café": 100,
}

cls()

#Apresenta o programa
print(art)
print('Bem-vindo à máquina de café!')
print('')

def coffee_machine():
    #Funções
    #Apresenta os recursos na tela
    def display_resources():
        for key in resources:
            value = resources[key]
            print(f'{key}: {value} ml')

    #Pergunta em loop qual café o usuário deseja
    def ask_user():
        cls()
        #Loop para caso o usuário digite algo errado
        choice_condition = True
        while choice_condition:
            user_choice = input(f'Digite o nome do café que você deseja: Espresso (R$ {menu["Espresso"]["cost"]}), Latte (R$ {menu["Latte"]["cost"]}) ou Cappuccino (R$ {menu["Cappuccino"]["cost"]})\n').title()

            #Caso a escolha seja a mesma do menu, procede o serviço
            for key in menu:
                if user_choice == key:
                    choice_condition = False
        return user_choice

    #Verificar se tem recursos suficiente
    def check_resource(coffee_ingredients, machine_resources):
        for ingredient in coffee_ingredients and machine_resources:
            #Acessa os valores do dicionário de recursos e ingredientes dos cafés
            coffee_value = coffee_ingredients[ingredient]
            machine_value = machine_resources[ingredient]

            #Verifica se a máquina tem recurso suficiente
            #Caso tenha, procede com o serviço
            if coffee_value <= machine_value:
                return True
            #Caso não tenha, cancela o procedimento do serviço
            else:
                return False

    #Subtrai o recurso para fazer um café
    def subtract_resource(coffee_ingredients):
        for ingredient in coffee_ingredients:
            #Acessa o valor do ingrediente do café
            ingredient_value = coffee_ingredients[ingredient]
            #Subtrai de acordo com o valor do ingrediente do café
            resources[ingredient] -= ingredient_value


    #Faz o café caso tenha recursos suficientes
    def machine_condition():
        #Verifica a condição retornada pela função check_resource
        #Caso a condição seja verdadeira, procede com o serviço
        if check_condition == True:
            subtract_resource(menu[user_coffee]["ingredients"])
        #Caso a condição seja falsa, encerra o procedimento apresentando o problema
        else:
            print('A cafeteira não tem recursos suficiente')
            coffee_machine()
    
    #Pergunta quanto o usuário deseja pagar
    def ask_payment():
        #Loop para evitar encerramento do programa caso o valor seja inválido
        while True:
            try:
                return float(input('Digite quanto você irá pagar\n'))
            except ValueError:
                print('Valor inválido, por favor digite um valor numérico')
                pass
    
    #Verifica o pagamento
    def check_payment(coffee_price, user_money):
        transaction_result = user_money - coffee_price

        if transaction_result < 0:
            print(f'Não foi possível efetuar o pagamento, valor insuficiente.')
            print(f'Retornando R$ {user_money} como reembolso.')
        elif transaction_result == 0:
            print('Pagamento efetuado com sucesso!')
            print(f'Seu café {user_coffee} está pronto!') #Faz o café
        else:
            print(f'Pagamento efetuado com sucesso! Devolvendo R$ {transaction_result} em troco.')
            print(f'Seu café {user_coffee} está pronto!') #Faz o café

    #Escolha do usuário
    while True:
        user_option = input('''Digite "coffee" para fazer seu café, "report" para verificar os recursos restantes ou "off" para desligar a máquina e realizar manutenções\n''')
        
        if user_option == "coffee":
            #Pergunta ao usuário qual café deseja
            user_coffee = ask_user()
            #Verifica a condição dos recursos da maquina
            check_condition = check_resource(menu[user_coffee]["ingredients"], resources) #True caso tenha / False caso não tenha
            machine_condition()
            #Processa o pagamento
            coffee_cost = menu[user_coffee]["cost"]
            #Verifica a transação
            user_payment = ask_payment()
            check_payment(coffee_cost, user_payment)

        #Apresenta o report
        elif user_option == "report":
            cls()
            print('Aqui estão os recursos restantes:')
            #Apresenta os recursos atuais da máquina
            display_resources()

        #Encerra o programa
        elif user_option == "off":
            print("Desligando maquina")
            print('Programa desenvolvido por Felipe :^)')
            exit()

        #Em questão de erro de digitação/escolha, refaz a pergunta
        else:
            print('Não é uma opção válida')
            True

coffee_machine()
