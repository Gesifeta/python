from operator import index
from turtle import Turtle
import time
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple","red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 15
MOVE_INCREMENT = 10


class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.level ="normal"
    def start(self,color):
        self.setposition(300,random.randint(-250,300)+STARTING_MOVE_DISTANCE)
        self.color(color)
        self.shape('square')
        self.speed("slow")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=2)
    def play(self):
        self.clear()
        self.setheading(180)
        self.forward(random.randint(1,40))
        if self.xcor() < -280:
            self.goto(250, random.randint(-250, 300))

