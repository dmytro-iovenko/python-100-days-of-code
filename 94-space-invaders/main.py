from turtle import Screen, Turtle
from player import Player
import time

#Set up screen                                         
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Space Invaders")
screen.tracer(0)

#Create the player
player = Player()

#Create keyboard bindings
screen.listen()
screen.onkey(key='Left', fun=player.move_left)
screen.onkey(key='Right', fun=player.move_right)
 
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.01)


screen.exitonclick()
