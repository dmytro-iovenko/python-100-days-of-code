from turtle import Screen, Turtle
from player import Player
from bullet import Bullet
import time

#Set up screen                                         
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Space Invaders")
screen.tracer(0)

#Create the player
player = Player()

#Create the bullet
bullet = Bullet()

#Create keyboard bindings
screen.listen()
screen.onkeypress(key='Left', fun=player.move_left)
screen.onkeypress(key='Right', fun=player.move_right)
screen.onkey(key='space', fun=lambda player=player: bullet.fire(player))
 
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.01)

    #Move the bullet
    if bullet.state == "fire":
        bullet.move()

    #Check to see if the bullet has gone to the top
    if bullet.ycor() > 275:
        bullet.reset()

screen.exitonclick()
