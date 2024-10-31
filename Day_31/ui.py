from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"

class QuizInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain

        #Config da janela
        self.window = Tk()
        self.window.title('Quizz App')
        self.window.config(padx=20, pady=20, background=THEME_COLOR)

        #Label config
        self.score_label = Label(text=f'Score: {self.quiz.score}', fg='white', bg=THEME_COLOR, padx=20, pady=20)
        self.score_label.grid(row=0, column=1)
        
        #Canvas config
        self.canvas = Canvas(width=300, height=250)
        self.question_text = self.canvas.create_text(150, 125, width=280, text='Question?', font=('Arial', 20, 'italic'), fill=THEME_COLOR)
        self.canvas.grid(row=1, column=0, columnspan=2, padx=20, pady=20)

        #Imagens
        self.true_img = PhotoImage(file='100days_python/Day_31/images/true.png')
        self.false_img = PhotoImage(file='100days_python/Day_31/images/false.png')
        
        #Botões
        self.true_button = Button(image=self.true_img, activebackground=THEME_COLOR, highlightthickness=0, borderwidth=0, command=self.true_answer)
        self.true_button.grid(row=2, column=0, padx=20, pady=20)

        self.false_button = Button(image=self.false_img, activebackground=THEME_COLOR, highlightthickness=0, borderwidth=0, command=self.false_answer)
        self.false_button.grid(row=2, column=1, padx=20, pady=20)

        self.get_next_question()

        self.window.mainloop()

    #Avança para a próxima questão
    def get_next_question(self):
        self.canvas.config(bg='white')
        if self.quiz.still_has_questions():
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.question_text, text=q_text)
            self.score_label.config(text=f'Score: {self.quiz.score}')
        else:
            self.canvas.itemconfig(self.question_text, text='Você concluiu o quiz!')
            self.true_button.config(state='disabled')
            self.false_button.config(state='disabled')

    #Funções dos botões
    def true_answer(self):
        self.give_feedback(self.quiz.check_answer('true'))

    def false_answer(self):
        self.give_feedback(self.quiz.check_answer('false'))

    def give_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg='green')
        else:
            self.canvas.config(bg='red')
        
        self.window.after(1000, self.get_next_question)