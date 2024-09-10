def add(n1, n2):
    return n1 + n2

def subtract(n1, n2):
    return n1 - n2

def multiply(n1, n2):
    return n1 * n2

def divide(n1, n2):
    return n1 / n2

operations_dict = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}

print('Projeto de calculadora')

def new_calculation(n1, op, n2):
    result = operations_dict[f"{op}"](n1, n2)
    print(f'{n1} {op} {n2} = {result}')
    return operations_dict[f"{op}"](n1, n2)
    
user_result = new_calculation(float(input('Digite seu primeiro número\n')), input('Digite "+", "-", "*" ou "/" para escolher um operador\n'), float(input('Digite seu segundo número\n')))


def continue_calculation(n1, op, n2):
    result = operations_dict[f"{op}"](n1, n2)
    print(f'{n1} {op} {n2} = {result}')
    return operations_dict[f"{op}"](n1, n2)

while True:
    user_choice = input('Digite "c" para continuar calculando, "n" para fazer um novo calculo ou "x" para finalizar\n')
    if user_choice == "c":
        user_result = continue_calculation(user_result, input('Digite "+", "-", "*" ou "/" para escolher um operador\n'), float(input('Digite um número\n')))
    elif user_choice == "n":
        user_result = new_calculation(float(input('Digite seu primeiro número\n')), input('Digite "+", "-", "*" ou "/" para escolher um operador\n'), float(input('Digite seu segundo número\n')))
    elif user_choice == "x":
        print('Programa encerrado')
        break
    else:
        print('Opção inválida, tente novamente.')
        True