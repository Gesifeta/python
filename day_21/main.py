import  random
import time
import turtle

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=500,height=500)
screen.title("My snake game")
screen.tracer(0)
screen.listen()

positions =[(0,0),(-20,0),(-40,0)]
colors = ["purple","green","yellow"]
segments =[]

def move_up(seg):
    seg.setheading(90)

def move_left(seg):
    seg.setheading(180)

def move_down(seg):
    seg.setheading(270)

for position in positions:
    turtle.colormode(255)
    new_segment = turtle.Turtle("turtle")
    new_segment.pu()
    new_segment.color(random.choice(colors))
    new_segment.goto(position)
    segments.append(new_segment)

game_is_on =True
while game_is_on:
    screen.update()
    time.sleep(.1)
    for segment in segments:
        new_seg = segment
        new_seg.color()
        new_seg.forward(10)
        if segment.xcor() > 210:
            new_seg.setheading(90)
        if new_seg.ycor()>210:
            new_seg.setheading(180)
        if new_seg.xcor() < -150:
            new_seg.setheading(270)
        if new_seg.ycor()<-150:
            new_seg.setheading(0)
            if segment.xcor() > 210:
                new_seg.setheading(90)

screen.exitonclick()
