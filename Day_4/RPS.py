import random

#Pedra, papel e tesoura
Pedra = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)'''

Papel = '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)'''

Tesoura = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)'''

#Escolha do jogador
userChoice = int(input('''Digite 1 para Pedra, 2 para Papel e 3 para Tesoura\n'''))
if userChoice == 1:
    print(f'''Você escolheu Pedra {Pedra}''')
elif userChoice == 2:
    print(f'''Você escolheu Papel {Papel}''')
else:
    print(f'''Você escolheu Tesoura {Tesoura}''')
#Escolha da máquina
computerChoice = random.randint(1, 3)
if computerChoice == 1:
    print(f'''O computador escolheu Pedra {Pedra}''')
elif computerChoice == 2:
    print(f'''O computador escolheu Papel {Papel}''')
else:
    print(f'''O computador escolheu Tesoura {Tesoura}''')
#Comparação das escolhas
if userChoice == 1 and computerChoice == 2:
    print('''O computador venceu''')
elif userChoice == 2 and computerChoice == 1:
    print('''Você venceu''')
elif userChoice == 2 and computerChoice == 3:
    print('''O computador Venceu''')
elif userChoice == 3 and computerChoice == 2:
    print('''Você venceu''')
elif userChoice == 3 and computerChoice == 1:
    print('''O computador venceu''')
elif userChoice == 1 and computerChoice == 3:
    print('''Você venceu''')
else:
    print('''Essa rodada foi um empate''')