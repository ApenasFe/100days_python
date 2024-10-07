from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.hideturtle()
        self.penup()
        self.goto(x=-280, y=250)
        self.stage_level = 1
        self.update_level()
        
    def update_level(self):
        self.clear()
        self.write(f'Level: {self.stage_level}', font=FONT)

    def increase_level(self):
        self.stage_level += 1
        self.update_level()

    def game_over(self):
        self.teleport(-75, 0)
        self.write('GAME OVER', font=FONT)