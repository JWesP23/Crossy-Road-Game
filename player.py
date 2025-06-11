from turtle import Turtle

STARTING_POSITION = (0, -274)
MOVE_DISTANCE = 30
FINISH_LINE_Y = 260


class Player(Turtle):

    def __init__(self):
        super().__init__(shape= "turtle")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_wid=0.8, stretch_len=0.8)
        self.setpos(STARTING_POSITION)
        self.color("white")

    def go_to_start(self):
        self.setheading(90)
        self.setpos(STARTING_POSITION)

    def move_forward(self):
        self.setheading(90)
        self.forward(MOVE_DISTANCE)

    def move_left(self):
        if -280 < self.xcor():
            self.setheading(180)
            self.forward(MOVE_DISTANCE)

    def move_right(self):
        if self.xcor() < 275:
            self.setheading(0)
            self.forward(MOVE_DISTANCE)

    def move_down(self):
        if self.ycor() > -274:
            self.setheading(270)
            self.forward(MOVE_DISTANCE)

    def check_level_up(self):
        if self.ycor() >= 280:
            self.goto(STARTING_POSITION)
            return True