import turtle
import random

timm = turtle.Turtle()
turtle.colormode(255)
timm.pensize(20)
screen = turtle.Screen()
directions = [0, 90,180,270]
def random_color():
    r = random.randint(0 ,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colors = (r,g,b)
    return random_colors
def play(num):
    for _ in range(num):
        timm.color((random_color()))
        timm.forward(20)
        timm.setheading(random.choice(directions))
        timm.forward(15)
play(100)




screen.exitonclick()

