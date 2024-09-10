from ascii_art import logo
import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

bidder_dictionary = {

}

print(logo)
print('Boas-vindas ao programa de Leilão Selado!')
while True:
    user_name = input('Digite o seu nome\n').title()
    user_bid = float(input('Digite a sua oferta\n'))
    bidder_dictionary[user_name] = user_bid

    user_choice = input('Tem outra pessoa que deseja fazer uma oferta? Digite "sim" ou "não"\n').lower()
    if user_choice == "não":
        highest_bid = max(bidder_dictionary.values())
        bid_winner = max(bidder_dictionary.keys())
        print(f'{bid_winner} venceu o leilão com uma oferta de R$ {round(highest_bid, 2)}')
        break
    cls()