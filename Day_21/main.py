from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard

screen = Screen()
screen.tracer(0)
screen.bgcolor('black')
screen.setup(width=800, height=600)
screen.title('Jogo Pong')

r_paddle = Paddle()
r_paddle.goto(x=350, y=0)

l_paddle = Paddle()
l_paddle.goto(x=-350, y=0)

ball = Ball()
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.up, 'Up')
screen.onkey(r_paddle.down, 'Down')
screen.onkey(l_paddle.up, 'w')
screen.onkey(l_paddle.down, 's')

game_is_on = True
while game_is_on:
    screen.update()
    ball.move()
    scoreboard.update_score()
    time.sleep(ball.move_speed)

    #Colisão da bola com as paredes
    if ball.ycor() > 270 or ball.ycor() < -270:
        ball.wall_bounce()

    #Colisão da bola com as raquetes
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.paddle_bounce()

    #Verifica se a bola passou o limite da tela
    if ball.xcor() > 390:
        scoreboard.l_point()
        ball.reset()
        time.sleep(3)
    
    elif ball.xcor() < -390:
        scoreboard.r_point()
        ball.reset()
        time.sleep(3)

screen.exitonclick()