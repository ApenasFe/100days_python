from tkinter import *
import pandas as pd
import random
from tkinter import messagebox
BACKGROUND_COLOR = "#B1DDC6"
WHITE_BACKGROUND = '#FFFFFF'
FONT_NAME = 'Ariel'

#--------------- WINDOW CONFIG ---------------
window = Tk()
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)
window.title('Aplicativo Flash Card')

#----------------- DADOS -----------------
try:
    word_df = pd.read_csv('100days_python/Day_28/data/learning_words.csv')
except FileNotFoundError:
    word_df = pd.read_csv('100days_python/Day_28/data/french_words.csv')
word_dict = word_df.to_dict(orient='records')

#---------- GERADOR DE PALAVRAS ----------
def new_word():
    try:
        global fr_en, flip_time
        window.after_cancel(flip_time)
        fr_en = random.choice(word_dict)
        canvas.itemconfig(canvas_image, image=front_img)
        canvas.itemconfig(card_title, text='French')
        canvas.itemconfig(card_text, text=fr_en['French'])
        flip_time = window.after(3000, flip_card)
    except (IndexError, ValueError, NameError):
        canvas.itemconfig(card_title, text='Aprendizado concluído!')
        canvas.itemconfig(card_text, text='Parabéns!')

#-------------- TROCA DE CARTÃO --------------
def flip_card():
    canvas.itemconfig(canvas_image, image=back_img)
    canvas.itemconfig(card_title, text='English')
    canvas.itemconfig(card_text, text=fr_en['English'])
flip_time = window.after(3000, flip_card)

#-------------- PALAVRA CONHECIDA --------------
def known_word():
    try:
        word_dict.remove(fr_en)
        data = pd.DataFrame(word_dict)
        data.to_csv('100days_python/Day_28/data/learning_words.csv')
        new_word()
    except (IndexError, ValueError, NameError):
        canvas.itemconfig(card_title, text='Aprendizado concluído!')
        canvas.itemconfig(card_text, text='Parabéns!')

#--------------------- UI --------------------
canvas = Canvas(width=800, height=526, highlightthickness=0, borderwidth=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file='100days_python/Day_28/images/card_front.png')
right_img = PhotoImage(file='100days_python/Day_28/images/right.png')
wrong_img = PhotoImage(file='100days_python/Day_28/images/wrong.png')
back_img = PhotoImage(file='100days_python/Day_28/images/card_back.png')

#Frente do cartão
canvas_image = canvas.create_image(400, 263, image=front_img)
canvas.grid(column=0, row=0, columnspan=2)

#Texto
card_title = canvas.create_text(400, 150, text='Titulo', font=(FONT_NAME, 40, 'italic'))
card_text = canvas.create_text(400, 263, text='Palavra', font=(FONT_NAME, 60, 'bold'))
try:
    new_word()
except IndexError:
    canvas.itemconfig(card_title, text='Aprendizado concluído!')
    canvas.itemconfig(card_text, text='Parabéns!')

#Botões
wrong_button = Button(image=wrong_img, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR, command=new_word)
wrong_button.grid(column=0, row=1)

right_button = Button(image=right_img, highlightthickness=0, bd=0, activebackground=BACKGROUND_COLOR, command=known_word)
right_button.grid(column=1, row=1)

#------------- WINDOW LOOP --------------
window.mainloop()