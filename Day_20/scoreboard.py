from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(0, 270)
        self.color('white')
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"Pontuação: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(f'FIM DE JOGO', align=ALIGNMENT, font=FONT)
    def scoring(self):
        self.score += 1
        self.update_score()