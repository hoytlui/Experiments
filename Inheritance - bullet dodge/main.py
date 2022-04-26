import time
from turtle import Screen
from bullet import Bullet
from player import Player
from scoreboard import Scoreboard


# set up screen
screen = Screen()
screen.setup(width=300, height=400)
screen.bgcolor('black')
screen.title('Bullet Dodge')
screen.tracer(0)

# create objects
player = Player()
bullet = Bullet()
scoreboard = Scoreboard()

# user control
screen.listen()
screen.onkey(player.go_up, "Up")
screen.onkey(player.go_down, "Down")
screen.onkey(player.go_left, "Left")
screen.onkey(player.go_right, "Right")

# start game
game_on = True
while game_on:
    # update screen every 0.1 sec
    screen.update()
    time.sleep(0.1)

    # create and move bullets
    bullet.create_bullet()
    bullet.move_bullet()

    # scenario: hit by bullet
    for b in bullet.bullet_list:
        if b.distance(player) < 10:
            game_on = False
            scoreboard.game_over()

    # scenario: finish one level
    if player.is_at_target():
        player.reset_pos()
        bullet.level_up()
        scoreboard.increase_level()

screen.exitonclick()