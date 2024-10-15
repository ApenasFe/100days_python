#Acessa, formata e armazena os dados em uma lista
def formated_list():
    #Acessa o local dos dados
    with open('100days_python/Day_23/Input/Names/invited_names.txt', mode='r') as data:
        name_list = data.readlines()
    
    #Lista vazia para armazenar os dados
    formated_list = []
    #Formata em loop todos os dados existentes
    for name in name_list:
        formated_name = name.strip('\n')
        formated_list.append(formated_name)
    #Retorna o valor da função com os dados formatados e armazenados
    return formated_list

#Dados formatados
name = formated_list()

#Cria uma carta de convite para festa à todos os convidados no arquivo invited_names.txt
def create_letter():
    #Faz um loop de acordo com o tamanho da lista
    for index in range(len(name)):
        #Acessa a carta de convite
        with open('100days_python/Day_23/Input/Letters/starting_letter.txt', mode='r', encoding='utf-8') as data:
            letter = data.read()
        #Reescreve a carta de acordo com o dado selecionado no loop e cria uma nova carta para os convidados
        with open(f'100days_python/Day_23/Output/ReadyToSend/letter_for_{name[index]}.txt', mode='w', encoding='utf-8') as data:
            #Cria o cartão para os convidados
            data.write(letter.replace('[name]', name[index]))

create_letter()
