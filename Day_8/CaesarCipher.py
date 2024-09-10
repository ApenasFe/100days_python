import os
def cls():
    os.system('cls' if os.name=='nt' else 'clear')

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

while True:

    user_choice = input('Digite "encode" para criptografar ou "decode" para descriptografar\n').lower()
    cls()
    user_message = input('Digite a mensagem\n').lower()
    cls()
    user_shift = int(input('Digite o número de substituições\n'))
    cls()

    def caesar(user_text, shift_amount, encode_decode):
        encrypted_message = ''
        
        if encode_decode == "decode":
            shift_amount *= -1

        for user_letter in user_text:

            encryptedIndex = alphabet.index(user_letter) + shift_amount
            encryptedIndex %= len(alphabet)
            encryptedChar = alphabet[encryptedIndex]
            encrypted_message += encryptedChar

        print(f'Resultado da sua mensagem é: {encrypted_message}')

    caesar(user_message, user_shift, user_choice)
    
    exit_continue = input('Digite "sair" para sair do programa ou "continuar" para utiliza-lo novamente\n').lower()
    if exit_continue == 'sair':
        print('Programa finalizado')
        break
    cls()