from turtle import Turtle
MOVE_DISTANCE = 20

class Paddle(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.shapesize(stretch_len=1, stretch_wid=5)
        self.color('white')
        self.speed('fastest')
        self.penup()

    def up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(x=self.xcor(), y=new_y)

    def down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(x=self.xcor(), y=new_y)