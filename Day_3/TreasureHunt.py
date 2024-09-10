import time
import os
clear = lambda: os.system('cls') #on Windows System
os.system('clear') #on Linux System

#Introdução ao jogo
print('''*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/______/
*******************************************************************************
Boas-vindas ao caça tesouros, você é um arqueólogo curioso, e um rumor sobre um artefato escondido nessa caverna te encheu de interesse. Boa sorte em sua jornada!
AVISO: Por incapacidade do desenvolvedor, erro de digitação pode levar a erro e fechar o jogo. Caso tenha certeza de que digitou corretamente então realmente pode ser erro no código.''')
time.sleep(2)
input('pressione "enter" para jogar\n')
clear()

#Entrada da caverna
entranceChoice = input('Ao entrar na caverna, você vê dois caminhos. Qual lado deseja seguir? Digite "esquerda" ou "direita".\n')

if entranceChoice == "esquerda":
    print('''------------------------------------------------------------------------------
Ao seguir para a esquerda, você é surpreendido por um bando de bandidos.
FIM DE JOGO
------------------------------------------------------------------------------''')
    time.sleep(5)
    quit()
elif entranceChoice == "direita":
    caveChoice = input('''------------------------------------------------------------------------------
Chegando no local, você vê algo brilhando em uma poça d'água e uma caixa aberta. O que deseja fazer? 
Digite "brilhante" ou "caixa".\n''')
else:
    print('Anomalia detectada, fechando jogo... (EntranceError)')
    time.sleep(5)
    quit()

#Em meio a caverna
if caveChoice == "brilhante":
    bridgeChoice = input('''------------------------------------------------------------------------------
Ao analisar a poça com cautela, você decide tomar coragem e pegar o objeto brilhante da poça. É um anél com a letra "D". Recuperando o anel, você avista uma ponte suspensa danificada. O que deseja fazer?
Digite "esperar" ou "atravessar"\n''')
elif caveChoice == "caixa":
    print('''------------------------------------------------------------------------------
Decidido em ver o que tem na caixa, uma cobra repentinamente pula em você te picando. Mesmo com um curativo no ferimento, você morre pelo veneno.
FIM DE JOGO
------------------------------------------------------------------------------''')
    time.sleep(5)
    quit()
else:
    print('Anomalia detectada, fechando jogo... (CaveError)')
    time.sleep(5)
    quit()

#Durante a ponte
if bridgeChoice == "atravessar":
    crossingChoice = input('''------------------------------------------------------------------------------
Sem pensar, você atravessa a ponte cuidadosamente, ficando em alerta com cada estalo das cordas. Após um tempo de tensão, você finalmente atravessa a ponte. Ao olhar para o lado, você avista um caminho e figuras na parede. O que você faz?
digite "analisar" para verificar a pintura ou "continuar" para seguir o caminho.\n''')
elif bridgeChoice == "esperar":
    print('''------------------------------------------------------------------------------
Esperando e analisando a ponte, hesitante sobre atravessar. Um bando de bandidos te encontra no caminho para a ponte. Desesperado você tenta atravessar a ponte correndo, porém a ponte se rompe e você cai.
FIM DE JOGO
------------------------------------------------------------------------------''')
    time.sleep(5)
    quit()
else:
    print('Anomalia detectada, fechando jogo... (Bridge Error)')
    time.sleep(5)
    quit()

#Durante o caminho
if crossingChoice == "analisar":
    pathChoice = input('''------------------------------------------------------------------------------
Analisando as figuras, você percebe que na verdade é uma mensagem. "Não acredite no sapo!". Confuso você segue o caminho da caverna.
Digite "continuar".\n''')
elif crossingChoice == "continuar":
    pathChoice = input('''------------------------------------------------------------------------------
Continuando o caminho, você se depara com 3 animais. 

O lobo cujo nome é Sapo, a raposa que se chama Lea e por fim o sapo Tony.

Reservado e suspeito o Sapo diz: "8"
A Lea pega sua mão e apresenta um sinal de "=".
O Tony, totalmente sério diz: "Nunca acredite no Sapo, o número correto é "5"!.

Após toda a conversa confusa, os três liberam o caminho aonde você continua sua jornada.
Digite "avançar" para seguir o caminho.\n''')

if pathChoice == "continuar":
    pathChoice = input('''------------------------------------------------------------------------------
Continuando o caminho, você se depara com 3 animais. 

O lobo cujo nome é Sapo, a raposa que se chama Lea e por fim o sapo Tony.

Reservado e suspeito o Sapo diz: "8"
A Lea pega sua mão e apresenta um sinal de "=".
O Tony, totalmente sério diz: "Nunca acredite no Sapo, o número correto é "5"!.

Após toda a conversa confusa, os três liberam o caminho aonde você continua sua jornada.
Digite "avançar" para seguir o caminho.\n''')

#Dentro da sala do cofre
if pathChoice == "avançar":
    vaultChoice = input('''------------------------------------------------------------------------------
Chegando no fundo da caverna, você vê um cofre com dispositivos estranho e uma senhora te cumprimentando. O que você deseja fazer?
Digite "verificar" para verificar o cofre ou "cumprimentar" para responder a senhora.\n''')
else:
    print('Anomalia detectada, fechando jogo... (VaultError)')
    time.sleep(5)
    quit()

if vaultChoice == "cumprimentar":
 terminalChoice = input('''------------------------------------------------------------------------------
Cumprimentando a senhora respeitosamente, você segue ao dispositivo misterioso.Entretando, muito barulho se aproxima de sua direção, como a guardiã do local, a senhora fecha o portão principal, evitando qualquer invasão.
Verificando o dispositivo, você percebe que na verdade é um terminal com 4 teclas, sim... 4 teclas.
Após apertar qualquer botão por pura curiosidade, o terminal pergunta se você deseja ler o dialógo. 
Aceitar?
"sim" / "não"\n''')
    
elif vaultChoice == "verificar":
    print('''------------------------------------------------------------------------------
Ignorando a senhora, você percebe que ela na verdade era um espectro e se torna cada vez mais e mais transparente, até desaparecer.
Confuso você segue ao dispositivo misterioso. 
Entretanto, passos são escutados indo em sua direção. 
Em curto periodo, você é cercado por um bando de bandidos.
FIM DE JOGO
------------------------------------------------------------------------------''')
    time.sleep(5)
    quit()
    
else:
    print('Anomalia detectada, fechando jogo...(VaultError)')
    time.sleep(5)
    quit()

#Utilizando o terminal
if terminalChoice == "sim":
   passChoice = input('''------------------------------------------------------------------------------
O lobo e o sapo cresceram juntos em uma floresta.
Com bom coração, a raposa os chamou para viver com ela em sua caverna.
No caminho da caverna, um anél caiu da bolsa da raposa. Nenhum dos 3 perceberam.

Digite a senha:\n''')
    
elif terminalChoice == "não":
   passChoice = input('''------------------------------------------------------------------------------
Digite a senha:\n''')

else:
    print('Anomalia detectada, fechando jogo...(TerminalError)')
    time.sleep(5)
    quit()

if passChoice == "8=D":
    print('''------------------------------------------------------------------------------
Com a senha correta, o cofre e um caminho secreto se abrem, você encontrou o tesouro perdido e saiu ileso da caverna!
Final A: Verdadeiro caçador de tesouros.
------------------------------------------------------------------------------''')
    time.sleep(5)
    input('Pressione enter para sair')

elif passChoice != "8=D":
    print('''------------------------------------------------------------------------------
Ao errar a senha, o dispositivo é desligado e o local começa a desmoronar. 
Apesar de todo seu esforço, você não encontrou nenhum jeito de escapar.
FINAL B: Nunca acredite no sapo.
------------------------------------------------------------------------------''') 
    time.sleep(5)
    input('Pressione enter para sair')