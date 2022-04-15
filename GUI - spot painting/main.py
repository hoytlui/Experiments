import turtle
import random


# colors used in the painting
color_list = [
    (255, 165, 0), (255, 193, 37), (137, 107, 211), (143, 188, 143), (229, 206, 206), 
    (102, 153, 204), (0, 156, 139), (200, 238, 230), (218, 170, 205), 
    (212, 94, 144), (105, 139, 105), (196, 114, 145), (222, 119, 106), 
    (210, 180, 140), (112, 147, 219), (205, 38, 38), (255, 215, 0), (153, 204, 50)
]

# set color mode in rgb
turtle.colormode(255)

# create object
arrow = turtle.Turtle()

# set speed
arrow.speed("fastest")

# hide trace
arrow.penup()

# hide turtle
arrow.hideturtle()

# set initial pos
arrow.setposition(-160, 160)
# get x, y
x, y = arrow.pos()

# set total spots and structure of the painting
total_spots = 64
spots_per_row = 8
for num_spot in range(1, total_spots + 1):
    arrow.dot(20, random.choice(color_list))
    arrow.forward(40)

    # when max spots per row filled out, go to the new line
    if num_spot % spots_per_row == 0:
        y -= 40
        arrow.setposition(x, y)


# set up GUI object
screen = turtle.Screen()
screen.screensize(500, 500)
screen.exitonclick()
