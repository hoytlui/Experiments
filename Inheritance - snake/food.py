from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)    # original 20x20, now 10x10
        self.color('white')
        self.speed('fastest')
        self.penup()
        self.refresh()

    def refresh(self):
        self.clear()
        self.goto(random.randint(-190, 170), random.randint(-190, 170))
