from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global reps
    reps = 0
    window.after_cancel(timer)
    canvas.itemconfig(timer_count, text='00:00')
    timer_label.config(text='Tempo')
    checkmark.config(text='')

# ---------------------------- TIMER MECHANISM ------------------------------- # 
def start_timer():
    global reps
    reps += 1
    
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 2 != 0:
        countdown(work_sec)
        timer_label.config(text='Tarefa', fg=GREEN)
    elif reps % 2 == 0 and reps != 8:
        countdown(short_break_sec)
        timer_label.config(text='Intervalo', fg=PINK)
    elif reps == 8:
        countdown(long_break_sec)
        reps = 0
        timer_label.config(text='Descanso', fg=RED)
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def countdown(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    canvas.itemconfig(timer_count, text=f'{count_min}:{count_sec}')
    if count > 0:
        global timer
        timer = window.after(1000, countdown, count - 1)
    else:
        start_timer()
        marks = ''
        work_sessions = math.floor(reps/2)
        for _ in range(work_sessions):
            marks += '✔'
        checkmark.config(text=marks)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title('Pomodoro')
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file='100days_python/Day_26/tomato.png')
canvas.create_image(100, 112, image=tomato_img)
timer_count = canvas.create_text(100, 130, text='00:00', fill='white', font=(FONT_NAME, 35, 'bold'))
canvas.grid(column=1, row=1)

timer_label = Label(text='Tempo', font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)
timer_label.grid(column=1, row=0)

start_button = Button(text='Iniciar', highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

checkmark = Label(fg=GREEN, bg=YELLOW)
checkmark.grid(column=1, row=3)

reset_button = Button(text='Reiniciar', highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

window.mainloop()