from turtle import Turtle, Screen
import random
import turtle

a_turtle = Turtle()
turtle.colormode(255)
a_turtle.penup()
a_turtle.hideturtle()
a_turtle.speed(25)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b

def set_start():
    a_turtle.setheading(215)
    a_turtle.forward(500)
    a_turtle.setheading(0)

def dot_gen(rgb):
    a_turtle.color(rgb)
    a_turtle.dot(30)
    a_turtle.forward(90)

def reposition():
    a_turtle.setheading(90)
    a_turtle.forward(90)
    a_turtle.setheading(180)
    a_turtle.forward(900)
    a_turtle.setheading(0)

def draw():
    set_start()
    
    i = 0
    while i < 8:
        for _ in range(0, 10):
            dot_gen(random_color())

        reposition()
        i += 1

draw()
screen = Screen()
screen.exitonclick()
