import random
from turtle import Turtle
import time

class Ball(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("circle")
        self.color("blue")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.pu()
        self.goto(position)
    def move_right(self,x,y):
        self.setheading(random.randint(x,y))
        while self.xcor()<=320:
            time.sleep(.1)
            self.forward(10)
        self.color("black")
    def move_left(self,x,y):
        self.setheading(random.randint(x,y))
        while self.xcor()>=-320:
            time.sleep(.1)
            self.forward(10)
        self.color("black")

