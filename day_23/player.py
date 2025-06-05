from turtle import Turtle, Screen

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 5
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("green")
        self.penup()
        self.setheading(90)
        self.setposition(STARTING_POSITION)
    def move_up(self):
        self.forward(MOVE_DISTANCE)
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
    def move_left(self):
        self.goto(self.xcor() - MOVE_DISTANCE, self.ycor())
    def move_right(self):
        self.goto(self.xcor() + MOVE_DISTANCE, self.ycor())

