from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(1000, 800)
user_input = screen.textinput("Corriga tartaruga", "Digite a cor da tartaruga que deseja apostar. (red, orange, yellow, green, blue, purple)").lower()
y_position = [-100, -50, 0, 50, 100, 150]
turtle_colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []
is_race_on = False

for turtle_index in range(0, 6):
    a_turtle = Turtle("turtle")
    a_turtle.color(turtle_colors[turtle_index])
    a_turtle.penup()
    a_turtle.goto(-450, y_position[turtle_index])
    all_turtles.append(a_turtle)

if user_input:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 470:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_input:
                print(f'Você venceu! A tartaruga {winning_color} ganhou a corrida.')
            else:
                print(f'Você perdeu! A tartaruga {winning_color} ganhou a corrida.')
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()