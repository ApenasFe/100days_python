import random
import time
import os

def cls():
    os.system('cls' if os.name=='nt' else 'clear')

#Deck (infinito)
card = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Função de finalizar ou reiniciar o jogo
def exit_continue():
    user_choice = input('Digite "r" para jogar novamente ou "e" para sair\n').lower()
    if user_choice == "r":
        blackjack()
    elif user_choice == "e":
        print('''Obrigado por jogar!
Projeto feito por Felipe :^)''')
        exit()

def blackjack():
    #deck dos participantes
    dealer_deck = []
    player_deck = []

    cls()
    #Função para alterar o valor de 11 para 1 caso tenha repetição de 11 nos decks
    def verify_deck():
        if player_deck[0] == 11 and player_deck [1] == 11:
            player_deck[0] = 1

        if dealer_deck[0] == 11 and dealer_deck [1] == 11:
            dealer_deck[0] = 1

    #Função para selecionar e distribuir cartas aleatórias aos participantes
    def shuffle():
        #Entrega cartas ao jogador
        i = 0
        p_shuffle_score = 0
        while i < 2:
            random_pick = random.choice(card)
            player_deck.append(random_pick)
            i += 1
            
        #Entrega cartas ao dealer
        i2 = 0
        d_shuffle_score = 0
        while i2 < 2:
            random_pick = random.choice(card)
            dealer_deck.append(random_pick)
            i2 += 1
        
        #Verifica se tem repetição de 11 para evitar 22
        verify_deck()
        
        #Calcula a pontuação dos participantes
        p_shuffle_score = player_deck[0] + player_deck[1]
        d_shuffle_score = dealer_deck[0] + dealer_deck[1]

        #Retorna a pontuação
        return p_shuffle_score, d_shuffle_score
    
    #Calcula a pontuação inicial dos participantes
    scores = shuffle() #Uma tupla com pontuação de todos
    player_score = scores[0] # Pontuação calculada do jogador
    dealer_score = scores[1] # Pontuação calculada do dealer

    #Rodada do jogador
    print(f'O primeiro número do dealer é: {dealer_deck[0]}')
    print(f'Seus números são: {player_deck} totalizando em {player_score}')

    #Função para dar uma carta ao jogador
    def player_hit():
        random_pick = random.choice(card)
        print(f'Você deu hit e puxou: {random_pick}')
        player_deck.append(random_pick)
        return random_pick

    #Escolha do jogador para "hit" ou "pass"
    while True:
        player_choice = input('Digite "h" para hit e pegar um número ou "p" para pass e terminar sua rodada.\n').lower()

        if player_choice == "h":
            player_score += player_hit() #Adiciona pontuação ao jogador
            print(f'Seus números são: {player_deck} totalizando em {player_score}')
            if player_score > 21: #Caso ultrapasse 21 o jogador perde
                print(f"Você perdeu por estourar 21 com: {player_deck} totalizando em {player_score}")
                exit_continue()
        elif player_choice == "p":
            cls()
            print(f'Você escolheu dar pass e seus números finais são: {player_deck} totalizando em {player_score}')
            break
        else:
            print('Essa opção não é válida')
            True
        

    #Rodada do dealer
    print('Iniciando a rodada do dealer...')
    #Função para dar uma carta ao dealer
    def dealer_hit():
        random_pick = random.choice(card)
        print(f'O dealer deu hit e puxou: {random_pick}')
        dealer_deck.append(random_pick)
        print(dealer_deck)
        return random_pick

    time.sleep(3)

    #Decisões do dealer
    while dealer_score < 17:
        dealer_score += dealer_hit() #Adiciona pontuação ao dealer
        if dealer_score > 21: #Caso o dealer ultrapasse 21 o dealer perde
            time.sleep(2)
            print(f"O Dealer perdeu por estourar 21 com os números: {dealer_deck} totalizando em {dealer_score}")
            exit_continue()
        time.sleep(3)
    print(f'O Dealer escolheu dar pass com os números finais: {dealer_deck} totalizando em {dealer_score}')
    time.sleep(3)

    #Compara o score do dealer e jogador
    if player_score > dealer_score:
        print(f'''Você venceu com {player_score}!
Seus números {player_deck} totalizando em {player_score}
Números do Dealer {dealer_deck} totalizando em {dealer_score}''')
    elif dealer_score > player_score:
        print(f'''O Dealer venceu com {dealer_score}!
Seus números {player_deck} totalizando em {player_score}
Números do Dealer {dealer_deck} totalizando em {dealer_score}''')
    else:
        print(f'''Vocês empataram com {player_score}
Seus números {player_deck} totalizando em {player_score}
Números do Dealer {dealer_deck} totalizando em {dealer_score}''')
    exit_continue()

blackjack()
