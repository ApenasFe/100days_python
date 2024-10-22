from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

#Carrega os dados salvos no saved_email.txt
with open('100days_python/Day_27/saved_email/saved_email.txt', 'r') as data_file:
    saved_email = data_file.read()

# ---------------------------- GERADOR DE SENHA ------------------------------- #

def gen_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    random_letters = [choice(letters) for _ in range(randint(8, 10))]
    random_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    random_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = random_letters + random_symbols + random_numbers
    shuffle(password_list)
    password = "".join(password_list)
    
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)
    

# ---------------------------- ARMAZENA DADOS ------------------------------- #
def save_data():
    #Pega e armazena os dados enviados em uma tupla
    data_tuple = (site_entry, password_entry)
    new_data_dict = {data_tuple[0].get().lower(): {
                    "Email": email_user_entry.get(),
                    "Password": data_tuple[1].get()
    }}

    #Valida se todos os campos do formulário foram preenchidos
    if len(data_tuple[0].get()) == 0 or len(email_user_entry.get()) == 0 or len(data_tuple[1].get()) == 0:
        messagebox.showwarning(title='Oops...', message='Por favor, não deixe nenhum campo vazio.')
    else:
        #Atualiza o arquivo JSON caso exista
        try:
            #Carrega e atualiza o antigo arquivo JSON
            with open('100days_python/Day_27/saved_password.json', 'r') as data_file:
                json_data = json.load(data_file)
                json_data.update(new_data_dict)    
            
            #Armazena os dados em JSON
            with open('100days_python/Day_27/saved_password.json', 'w') as data_file:
                json.dump(json_data, data_file, indent=4)
        
        #Cria um arquivo JSON caso não exista
        except FileNotFoundError:
            with open('100days_python/Day_27/saved_password.json', 'w') as data_file:
                json.dump(new_data_dict, data_file, indent=4)

        #Atualiza e salva o email no campo
        with open('100days_python/Day_27/saved_email/saved_email.txt', 'w') as saved_data_file:
            saved_data_file.write(email_user_entry.get())
        
        #Após adicionar os dados no arquivo, faz um loop deletando os dados no campo do formulário
        for data in data_tuple:
            data.delete(0, END)

# ---------------------------- FUNÇÃO DE PROCURA ------------------------------- #
def search_data():
    search_entry = site_entry.get()
    try:
        with open('100days_python/Day_27/saved_password.json', 'r') as data_file:
            json_data = json.load(data_file)
            messagebox.showinfo(title=search_entry, message=f'Email/Username: {json_data[search_entry.lower()]['Email']} \nSenha: {json_data[search_entry.lower()]['Password']}')
    except (KeyError, FileNotFoundError):
            messagebox.showwarning(title='Erro', message=f'Nenhum dado do site "{search_entry}" foi encontrado.')

# ---------------------------- CONFIGURAÇÃO UI ------------------------------- #

#Config da janela
window = Tk()
window.title('Gerenciador de senha')
window.config(padx=20, pady=20)

#Config do logo
canvas = Canvas(width=200, height=200)
logo_img = PhotoImage(file='100days_python/Day_27/logo.png')
canvas.create_image(100, 100, image=logo_img)
canvas.grid(column=1, row=0)

#Labels
site_label = Label(text='Nome do site:')
site_label.grid(column=0, row=1)

email_user_label = Label(text='Email/Username:')
email_user_label.grid(column=0, row=2)

password_label = Label(text='Senha:')
password_label.grid(column=0, row=3)

#Entries
site_entry = Entry()
site_entry.grid(column=1, row=1, sticky='EW')
site_entry.focus()

email_user_entry = Entry()
email_user_entry.grid(column=1, row=2, columnspan=2, sticky='EW')
email_user_entry.insert(0, saved_email)

password_entry = Entry()
password_entry.grid(column=1, row=3, sticky='EW')

#Botões
search_button = Button(text='Procurar', command=search_data)
search_button.grid(column=2, row=1, sticky='EW')

pass_gen_buttton = Button(text='Gerar senha', command=gen_password)
pass_gen_buttton.grid(column=2, row=3)

add_button = Button(text='Adicionar', command=save_data)
add_button.grid(column=1, row=4, columnspan=2, sticky='EW')

#Loop para manter janela aberta
window.mainloop()