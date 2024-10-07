import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title('Jogo Turtle Crossing')

player = Player()
scoreboard = Scoreboard()
all_cars = []

#Cria e armazena os carros criados
for _ in range(1, 16):
    initial_position = (random.randint(-300, 320), random.randint(-240, 250))
    new_car = CarManager()
    new_car.initial_position(x=initial_position[0], y=initial_position[1])
    all_cars.append(new_car)


screen.onkey(player.move, "Up")
screen.listen()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    
    #Manipula os carros armazenados na lista all_cars
    for car in all_cars:
        car.move()
        
        #Detecta se o carro chegou no limite designado e reposiciona aleatóriamente.
        if car.xcor() < -315:
            random_reposition = (random.randint(310, 400), random.randint(-240, 250))
            car.new_position(x=random_reposition[0], y=random_reposition[1])
        
        #Detecta se o jogador chegou ao outro lado e aumenta o nível e velocidade dos carros.
        if player.ycor() > 300:
            player.initial_position()
            scoreboard.increase_level()
            for car in all_cars:
                car.increase_speed()
        
    #Detecta colisão entre o carro e o jogador
        if player.distance(car) < 28:
            game_is_on = False
            scoreboard.game_over()
    

screen.exitonclick()