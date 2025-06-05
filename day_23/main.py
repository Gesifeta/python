import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from car_manager import  COLORS
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)

player = Player()
time.sleep(.1)

screen.onkey(player.move_up,"Up")
screen.onkey(player.move_right,"Right")
screen.onkey(player.move_left,"Left")
for color in COLORS:
    cards = CarManager()
    cards.penup()
    screen.update()
    time.sleep(.1)
    cards.start(color)
    time.sleep(.1)
while True:
    screen.update()
    time.sleep(.1)
    screen.update()
    time.sleep(.1)
