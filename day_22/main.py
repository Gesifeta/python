from turtle import Screen,Turtle

from paddle import Paddle
import  random
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)
screen.setup(height=600,width=800)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))




screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
game_is_on =True
while game_is_on:
    screen.update()
screen.exitonclick()