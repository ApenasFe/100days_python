from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape('square')
        self.shapesize(stretch_len=2)
        self.color(f'{random.choice(COLORS)}')
        self.setheading(180)
        self.move_speed = STARTING_MOVE_DISTANCE

    def initial_position(self, x, y):
        self.goto(x, y)
    
    def move(self):
        self.forward(self.move_speed)

    def new_position(self, x, y):
        self.teleport(x, y)

    def increase_speed(self):
        self.move_speed += MOVE_INCREMENT