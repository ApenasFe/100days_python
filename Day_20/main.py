from turtle import Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Jogo da cobra')
screen.tracer(0)

cobra = Snake()

screen.listen()
screen.onkey(cobra.up, 'Up')
screen.onkey(cobra.down, 'Down')
screen.onkey(cobra.left, 'Left')
screen.onkey(cobra.right, 'Right')

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.06)

    cobra.move()

screen.exitonclick()