from turtle import  Turtle,Screen
import random
timmy_the_turtle = Turtle()
screen = Screen()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("green")

def draw_shapes(number_of_sides):
    angles = round(360/number_of_sides,0)
    for _ in range(0,number_of_sides):
        timmy_the_turtle.forward(50)
        timmy_the_turtle.right(angles)
for num in range(3,10):
    draw_shapes(num)


