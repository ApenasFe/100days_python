import pandas

phonetic_df = pandas.read_csv('100days_python/Day_24/nato_phonetic_alphabet.csv')

#Cria um dicionário das letras do phonetic alphabet
phonetic_dict = {row.letter:row.code for (index, row) in phonetic_df.iterrows()}

#Cria uma lista com o input do usuário e apresenta o valor do phonetic alphabet
u_wordlist = list(input('Digite o seu nome:\n').upper())
u_phonetic_list = [value for u_letter in u_wordlist for (key, value) in phonetic_dict.items() if u_letter == key]

print(u_phonetic_list)