from turtle import Turtle


# global variables
FONT = ('Courier', 18, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-140, 170)
        self.update_score()

    def update_score(self):
        self.clear()
        self.pencolor('white')
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_level(self):
        self.level += 1
        self.update_score()

    def game_over(self):
        self.goto(0, 10)
        self.pencolor('white')
        self.write("GAME OVER", align="center", font=FONT)