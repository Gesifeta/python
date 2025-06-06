import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager, COLORS
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
time.sleep(.1)
cars = []

screen.onkeypress(player.move_up,"Up")
screen.onkeypress(player.move_right,"Right")
screen.onkeypress(player.move_left,"Left")

game_is_on = True
for color in COLORS:
    car = CarManager()
    cars.append(car)
while game_is_on:
    for car in cars:
        car.penup()
        car.shape("square")
        car.shapesize(stretch_wid=1, stretch_len=2)
        car.setposition(250, random.randint(-250,300)+ 10)
        car.color(COLORS[cars.index(car)])
        screen.update()
        time.sleep(.1)
    while game_is_on:
        for car in cars:
            if car.distance(player) < 10:
                game_is_on = False
            car.play()
        screen.update()
        time.sleep(.1)
        screen.update()
        time.sleep(.1)
    screen.exitonclick()
