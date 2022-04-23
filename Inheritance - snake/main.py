import time
from turtle import Turtle, Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard


# set up screen
screen = Screen()
screen.setup(width=460, height=460)
screen.bgcolor('black')
screen.title('Snake')
screen.tracer(0)    # turn off animation

# create objects
snake = Snake()
food = Food()
scoreboard = Scoreboard()
turtle = Turtle()

# draw arena
turtle.hideturtle()
turtle.penup()
turtle.color('white')
turtle.goto(-210, 190)
turtle.pendown()
for _ in range(4):
    turtle.forward(200*2)
    turtle.right(90)

# listen for keystroke
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

# game
game_on = True
while game_on:
    time.sleep(0.1)
    screen.update() # refresh screen once for loop executed
    snake.move()

    # scenario: collide with food
    if snake.head.distance(food) < 20:
        food.refresh()
        snake.extend()
        scoreboard.add_score()

    # scenario: bump into wall
    if snake.head.xcor() > 190 or snake.head.xcor() < -200 or snake.head.ycor() > 190 or snake.head.ycor() < -200:
        game_on = False
        scoreboard.game_over()
        
    # scenario: collide with own tail
    for block in snake.block_list[1:]:
        if snake.head.distance(block) < 10:
            game_on = False
            scoreboard.game_over()

screen.exitonclick()