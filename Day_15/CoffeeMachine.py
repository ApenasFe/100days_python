#Biblioteca

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

#Funções
#Apresenta os recursos na tela
def display_resources():
    for key in resources:
        value = resources[key]
        print(f'{key}: {value}')

#Pergunta em loop qual café o usuário deseja
def ask_user():
    #Loop para caso o usuário digite algo errado
    choice_condition = True
    while choice_condition:
        user_choice = input('Digite o nome do café que você deseja: Espresso, Latte ou Cappuccino\n').title()

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

        #Compara para checar se a máquina tem recurso suficiente
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
def make_coffe():
    #Verifica a condição retornada pela função check_resource
    #Caso a condição seja verdadeira, procede com o serviço
    if check_condition == True:
        subtract_resource(menu[user_decision]["ingredients"])
        print(f'Seu café {user_decision} está pronto!')
    #Caso a condição seja falsa, encerra o procedimento apresentando o problema
    else:
        print('A cafeteira não tem recursos suficiente')


#Apresenta o programa
print('Bem-vindo ao programa da máquina de café!')
print('')

#Escolha do usuário
while True:
    user_option = input('''Digite "coffee" para fazer seu café, "report" para verificar os recursos restantes ou "off" para desligar a máquina e realizar manutenções\n''')

    if user_option == "coffee":
        #Pergunta ao usuário qual café deseja
        user_decision = ask_user()
        #Verifica a condição dos recursos da maquina
        check_condition = check_resource(menu[user_decision]["ingredients"], resources) #True caso tenha / False caso não tenha
        #Faz o café
        make_coffe()

    #Apresenta o report
    elif user_option == "report":
        print('Aqui estão os recursos restantes:')
        #Apresenta os recursos atuais da máquina
        display_resources()

    #Encerra o programa
    elif user_option == "off":
        print("Desligando maquina")
        exit()

    #Em questão de erro de digitação/escolha, refaz a pergunta
    else:
        print('Não é uma opção válida')
        True

#3. Processar o pagamento
#4. Verificar se a transação foi efetuada
