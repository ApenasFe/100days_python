import random
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

cls()
#Introdução
print('Boas-vindas ao gerador de senha!')

#Quantas vezes será repetida a randomização
userLetters = int(input('Quantas letras deseja adicionar em sua senha?\n'))
cls()
userNumbers = int(input('Quantos números deseja adicionar em sua senha?\n'))
cls()
userSymbols = int(input('Quantos símbolos deseja adicionar em sua senha?\n'))
cls()

#Variáveis vazia para gerar senha
generatedPass = ('')

#Gerador de letras para a senha
for letterLoop in range(1, userLetters + 1):
    letterIndex = random.randint(0, 51)
    for letterAdd in letters[letterIndex]:
        generatedPass += letterAdd
#Gerador de números para a senha
for numberLoop in range(1, userNumbers + 1):
    numberIndex = random.randint(0, 9)
    for numberAdd in numbers[numberIndex]:
        generatedPass += numberAdd
#Gerador de caracteres especiais para a senha
for symbolLoop in range(1, userSymbols + 1):
    symbolIndex = random.randint(0, 8)
    for symbolAdd in symbols[symbolIndex]:
        generatedPass += symbolAdd

#Embaralha a senha gerada
newPassword = ('').join(random.sample(generatedPass,len(generatedPass)))

#Mostra nova senha gerada
print(f'Senha gerada: {newPassword}')
input('Pressione enter para sair')