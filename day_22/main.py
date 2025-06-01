from turtle import Screen,Turtle
import  random
screen = Screen()
paddle = Turtle()
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

screen.setup(height=600,width=800)

paddle.shape("square")
paddle.color("white")
paddle.shapesize(stretch_wid=5,stretch_len=1)
paddle.pu()
paddle.goto(350,0)
screen.update()
def move_up():
    new_y = paddle.ycor() + 20
    if new_y >= 300:
        return
    paddle.goto(paddle.xcor(),new_y)
def move_down():
    new_y = paddle.ycor() - 20
    if new_y <= -300:
        return
    paddle.goto(paddle.xcor(),new_y)

def move_paddle():
    is_game_on = True
    while is_game_on:
        paddle.goto(350,random.randint(-300,350),)
        paddle.speed("slowest")
# move_paddle()
screen.onkey(move_up,"Up")
screen.onkey(move_down,"Down")
screen.exitonclick()