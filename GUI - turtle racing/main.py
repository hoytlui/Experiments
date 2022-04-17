from turtle import Turtle, Screen
import random


# set up screen
screen = Screen()
screen.setup(width=500, height=400)

# get prompt from user
bet = screen.numinput(title='Make Your Bet', prompt='Select your favourite turtle to win: (1-7)')
num_turtle = 7
color_list = ['red3', 'tan2', 'yellow2', 'SeaGreen3', 'SteelBlue2', 'SlateBlue3', 'VioletRed']
y_pos = [-90, -60, -30, 0, 30, 60, 90]
turtle_list = []

for i in range(num_turtle):
    # create instance
    new_turtle = Turtle(shape='turtle')
    new_turtle.color(color_list[i])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_pos[i])
    turtle_list.append(new_turtle)

# draw finish line
finish_line = 200
line = Turtle()
line.pensize(10)
line.penup()
line.setpos(x=finish_line, y=120)
line.pendown()
line.setheading(-90)
line.forward(240)
line.hideturtle()

# loop while racing
game = True
while game:
    for turtle in turtle_list:
        if turtle.xcor() > finish_line - 20:
            game = False
            # find winning turtle
            winning_idx = (turtle.ycor() + 90) / 30
            if winning_idx == bet - 1:
                print(f"You win. Turtle {int(winning_idx + 1)} is the winner!")
            else:
                print(f"You lose. Turtle {int(winning_idx + 1)} is the winner!")

        turtle.forward(random.randint(0, 10))

# exit screen
screen.exitonclick()