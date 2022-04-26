import random
from turtle import Turtle


# global variables
MOVING_SPEED = 10
SPEED_INCREMENT = 1.5

class Bullet:

    def __init__(self):
        self.bullet_list = []
        self.bullet_speed = MOVING_SPEED

    def create_bullet(self):
        # apply probability to reduce occurrence of creating bullet
        random_num = random.randint(2, 4)
        if random_num % 2 == 0:
            new_bullet = Turtle('circle')
            new_bullet.color('orange')
            new_bullet.shapesize(stretch_wid=0.2, stretch_len=0.5)
            new_bullet.penup()
            new_bullet.setheading(-90)
            new_bullet.goto(random.randint(-260, 260), 200)
            self.bullet_list.append(new_bullet)

    def move_bullet(self):
        for bullet in self.bullet_list:
            bullet.forward(self.bullet_speed)

    def level_up(self):
        self.bullet_speed *= SPEED_INCREMENT
