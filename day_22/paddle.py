from turtle import  Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.pu()
        self.goto(position)

    def move_up(self):
        new_y = self.ycor() + 20
        if new_y >= 300:
            return
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor() - 20
        if new_y <= -300:
            return
        self.goto(self.xcor(), new_y)
