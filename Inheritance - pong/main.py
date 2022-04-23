import time
from turtle import Screen
from ball import Ball
from paddle import Paddle
from scoreboard import Scoreboard


# set up screen
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor('black')
screen.title('PONG')
screen.tracer(0)    # turn off animation

# position paddles
r_paddle = Paddle((360, 0))
l_paddle = Paddle((-360, 0))

# create objects
ball = Ball()
scoreboard = Scoreboard()

# listen for keystroke
screen.listen()
screen.onkey(r_paddle.go_up, 'Up')
screen.onkey(r_paddle.go_down, 'Down')
screen.onkey(l_paddle.go_up, 'w')
screen.onkey(l_paddle.go_down, 's')


# start game
winning_score = 3
game_on = True
while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    # scenario: ball collides with wall and bounces
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # scenario: ball collides with paddle
    if (ball.distance(r_paddle) < 50 and ball.xcor() > 340) or (ball.distance(l_paddle) < 50 and ball.xcor() < -340):
        ball.bounce_x()

    # scenario: paddle misses ball
    if ball.xcor() > 380:
        ball.reset_pos()
        scoreboard.add_score('l_score')
    
    if ball.xcor() < -380:
        ball.reset_pos()
        scoreboard.add_score('r_score')

    # scenario: game ends
    if scoreboard.l_score == winning_score or scoreboard.r_score == winning_score:
        scoreboard.end_game()
        game_on = False

screen.exitonclick()