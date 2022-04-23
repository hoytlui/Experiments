from turtle import Turtle


# global variables
ALIGNMENT = 'center'
FONT = ('Courier', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.show_score()

    def show_score(self):
        self.clear()
        self.goto(-50, 260)
        self.write(self.l_score, align=ALIGNMENT, font=FONT)
        self.goto(50, 260)
        self.write(self.r_score, align=ALIGNMENT, font=FONT)

    def add_score(self, side):
        if side == 'l_score':
            self.l_score += 1
        elif side == 'r_score':
            self.r_score += 1
        self.show_score()

    def end_game(self):
        self.clear()
        self.goto(0, 20)
        self.write("FINAL SCORE", align=ALIGNMENT, font=FONT)
        self.goto(0, -10)
        self.write(f"{self.l_score} vs {self.r_score}", align=ALIGNMENT, font=FONT)