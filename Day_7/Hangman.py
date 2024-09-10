import random
stages = [r'''
____
|/   |
|   
|    
|    
|    
|
|_____''',r'''
 ____
|/   |
|   (_)
|    
|    
|    
|
|_____''',r'''
 ____
|/   |
|   (_)
|    |
|    |    
|    
|
|_____''',r'''
 ____
|/   |
|   (_)
|   /|
|    |
|    
|
|_____''',r'''
 ____
|/   |
|   (_)
|   /|\
|    |
|    
|
|_____''',r'''
 ____
|/   |
|   (_)
|   /|\
|    |
|   | 
|
|_____''',r'''
 ____
|/   |
|   (_)
|   /|\
|    |
|   | |
|
|_____''']

#Seleciona uma palavra aleatória
wordList = ['rato', 'lampada', 'escova']
chosenWord = random.choice(wordList)

#Cria um placeholder para o usuário saber quantas letras tem a palavra escolhida
placeholder = ''
wordLenght = len(chosenWord)
for position in range(wordLenght):
    placeholder += '_'

#Mostra o total de letras ao usuário
print(placeholder)

#Lista de acertos
correctGuess = []
#Condição de jogo
gameOver = False
#Tentativas do usuário
userAttempts = -1
#Inicio do loop
while not gameOver:
    #Pergunta o chute do usuário e mostra o total de letras
    userGuess = input(f'Digite uma letra\n')
    #Atualiza e apresenta o resultado da escolha do usuário
    displayWord = ''
    
    #Mecânica principal do jogo
    for wordCheck in chosenWord:
        #Caso o chute do usuário for a mesma da atual letra
        if wordCheck == userGuess:
            #Adicione a letra do usuário ao display
            displayWord += wordCheck
            #Adiciona o chute do usuário a lista de chutes corretos
            correctGuess.append(userGuess)
        #Caso a letra atual já estiver na lista de chutes corretos
        elif wordCheck in correctGuess:
            #Adicione a letra atual ao display
            displayWord += wordCheck
       #Caso nenhuma das opções forem atingidas, adicione '_' ao display
        else:
            displayWord += '_'
    
    #Apresenta o display ao usuário
    print(displayWord)

    #Condição de vitória do usuário
    if '_' not in displayWord:
        gameOver = True
        print('Você venceu')
    
    #Condição de erro do usuário
    elif userGuess not in chosenWord:
        #Cada erro subtrai uma tentativa do usuário
        userAttempts += 1
        print(stages[userAttempts])
    
    #Condição de derrota do usuário
    #Caso acabe as tentativas, o usuário perde
    if userAttempts == 6:
        gameOver = True
        print('Você perdeu')