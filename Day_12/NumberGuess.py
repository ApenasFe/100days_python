#Biblioteca
import random
from ascii_art import art
import os

#Função para limpar interface do terminal de qualquer OS
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Apresenta o programa
cls() #Limpa a interface
print(art)
print('Bem-vindo! Esse é um jogo simples, adivinhe o número que eu escolher!')

def number_guess():
    #Função para reiniciar ou finalizar o programa
    def restart_exit():
        while True:
            #Escolha do jogador
            player_choice = input('Digite "r" para reiniciar ou "e" para sair.\n').lower()
            #Condição para reiniciar o programa
            if player_choice == "r":
                cls()
                number_guess()
                break
            #Condição para encerrar o programa
            elif player_choice == "e":
                print('''Obrigado por jogar!
Projeto feito por Felipe :^)''')
                exit()
            #Caso um valor inválido seja enviado, reinicia o loop
            else:
                print('Não é uma opção válida')
                True

    #Tentativas do jogador
    player_attempts = 0
    #Loop para evitar problemas com erros de digitação
    while True:
        #Pergunta a dificuldade ao jogador (Fácil = 10 | Difícil = 5)
        start_choice = input('''Irei pensar em um número entre 1 a 100.
Escolha uma dificuldade. Digite "f" para fácil ou "d" para dificil.\n''').lower()
        if start_choice == "f":
            print('Dificuldade fácil selecionada')
            #Ajusta a vida do jogador de acordo com a dificuldade
            player_attempts = 10
            break
        elif start_choice == "d":
            print('Dificuldade dificil selecionada')
            #Ajusta a vida do jogador de acordo com a dificuldade
            player_attempts = 5
            break
        #Caso um valor inválido seja enviado, reinicia o loop
        else:
            print('Não é uma opção válida')
            True

    #Escolhe um número entre 1 - 100
    random_pick = random.randrange(1, 101)

    #Faz um loop para as escolhas do jogador até a vida se esgotar
    while player_attempts > 0:
        #Pede o chute do jogador em tipo int
        player_guess = int(input('Chute um número\n'))
        
        #Compara a escolha do jogador com as condições do jogo
        #Condição de vitória
        if player_guess == random_pick:
            print(f'Parabéns! você acertou restando {player_attempts} tentativas e o número correto era {random_pick}.')
            restart_exit() #Perguntar se o jogador quer jogar novamente ou encerrar o programa
        #Chute muito alto
        elif player_guess > random_pick:
            player_attempts -= 1 #Subtrai uma vida do jogador
            cls()
            print(f'Você chutou: {player_guess}')
            print(f'Seu chute foi alto (tentativas restantes: {player_attempts})')
        #Chute muito baixo
        else:
            player_attempts -= 1
            cls()
            print(f'Você chutou {player_guess}')
            print(f'Seu chute foi baixo (tentativas restantes: {player_attempts})')

    #Caso a vida esgotar, finalizar o jogo e apresentar a resposta
    print(f'Você perdeu, o número correto era: {random_pick}') #Condição de derrota
    
    #Perguntar se o jogador quer jogar novamente ou encerrar o programa
    restart_exit()

#Inicializa o programa chamando a função number_guess()
number_guess()