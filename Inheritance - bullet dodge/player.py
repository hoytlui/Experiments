from turtle import Turtle


# global variables
STARTING_POS = (0, -160)
MOVING_DISTANCE = 10
FINISH_LINE = 160

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.color('green')
        self.penup()

        # draw finish line
        self.goto(-150, FINISH_LINE)
        self.pendown()
        self.pensize(5)
        self.pencolor('white')
        self.forward(300)
        self.penup()

        # position player
        self.reset_pos()
        self.setheading(90)

    def reset_pos(self):
        self.goto(STARTING_POS)

    def go_up(self):
        self.setheading(90)
        self.forward(MOVING_DISTANCE)

    def go_down(self):
        self.setheading(90)
        self.backward(MOVING_DISTANCE)

    def go_left(self):
        self.setheading(180)
        self.forward(MOVING_DISTANCE)

    def go_right(self):
        self.setheading(0)
        self.forward(MOVING_DISTANCE)

    def is_at_target(self):
        return self.ycor() > FINISH_LINE