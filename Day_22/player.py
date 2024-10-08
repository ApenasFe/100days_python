from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('black')
        self.penup()
        self.initial_position()
        self.setheading(90)

    def initial_position(self):
        self.teleport(x=STARTING_POSITION[0], y=STARTING_POSITION[1])

    def move(self):
        self.forward(MOVE_DISTANCE)

    