from turtle import Turtle


# global variables
ORIGINAL_SPEED = 0.1
SPEED_INCREMENT = 0.9

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('white')
        self.penup()
        self.move_x = 10
        self.move_y = 10
        self.ball_speed = ORIGINAL_SPEED

    def move(self):
        self.goto(self.xcor() + self.move_x, self.ycor() + self.move_y)

    def bounce_y(self):
        self.move_y *= -1
    
    def bounce_x(self):
        self.move_x *= -1
        self.ball_speed *= SPEED_INCREMENT

    def reset_pos(self):
        self.goto(0, 0)
        self.ball_speed = ORIGINAL_SPEED
        self.bounce_x()
