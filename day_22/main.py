from turtle import Screen,Turtle

from paddle import Paddle
from ball import Ball
import  random
screen = Screen()
screen.bgcolor("black")
screen.title("Pong")
screen.listen()

screen.setup(height=600,width=800)
r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
screen.onkey(l_paddle.move_up,"w")
screen.onkey(l_paddle.move_down,"s")
screen.onkey(r_paddle.move_up,"Up")
screen.onkey(r_paddle.move_down,"Down")
is_game_on =True
while is_game_on:
    r_ball = Ball((0, 0))
    r_ball.speed("slowest")
    r_ball.move_right(0,45)
    l_ball = Ball((0,0))
    l_ball.speed("slowest")
    l_ball.move_left(135,225)


screen.exitonclick()