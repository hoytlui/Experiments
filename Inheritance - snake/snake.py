from turtle import Turtle


# global variables
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = -90
LEFT = 180
RIGHT = 0

class Snake(Turtle):

    def __init__(self):
        self.block_list = []
        self.create_snake()
        self.head = self.block_list[0]

    def create_snake(self):
        for pos in STARTING_POS:
            self.add_block(pos)

    def add_block(self, pos):
        new_block = Turtle('square')
        new_block.color('white')
        new_block.penup()
        new_block.goto(pos)
        self.block_list.append(new_block)

    def extend(self):
        self.add_block(self.block_list[-1].position())

    def move(self):
        for i in range(len(self.block_list)-1, 0, -1):
            new_x = self.block_list[i-1].xcor()
            new_y = self.block_list[i-1].ycor()
            self.block_list[i].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
    
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)