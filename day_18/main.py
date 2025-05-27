from turtle import Turtle, Screen, Screen
import  random



timmy = Turtle()
screen = Screen()
random = random.random()
for i in range(100):
    steps = int(random * 100)
    angle = int(random* 360)
    timmy.right(angle)
    timmy.fd(steps)

timmy.screen.mainloop()
screen.exitonclick()