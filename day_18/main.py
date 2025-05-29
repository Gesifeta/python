from random import choice
from turtle import  Turtle,Screen
import random
timmy_the_turtle = Turtle()
screen = Screen()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

colors =["blue","bisque","orange","pink","purple","mediumOrchid"]
directions =[0, 90, 180, 270]
timmy_the_turtle.pensize(20)
timmy_the_turtle.speed("slowest")
for _ in range(1,100):
    timmy_the_turtle.color(random.choice(colors))
    timmy_the_turtle.forward(10)
    timmy_the_turtle.setheading(random.choice(directions))
    timmy_the_turtle.forward(20)



screen.exitonclick()


