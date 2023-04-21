from turtle import Screen, Turtle
from player import Player
from bullet import Bullet
from enemies import Enemies
from scoreboard import Scoreboard
import time
import math

#Set up screen                                         
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Space Invaders")
screen.tracer(0)

#Create the score board
score = Scoreboard(1)
#Create the player
player = Player()
#Create enemies
enemies = Enemies(1)
#Create the bullet
bullet = Bullet()

#Create keyboard bindings
screen.listen()
screen.onkeypress(key='Left', fun=player.move_left)
screen.onkeypress(key='Right', fun=player.move_right)
screen.onkey(key='space', fun=lambda player=player: bullet.fire(player))

def isCollision(t1,t2):
    distance = math.sqrt(math.pow(t1.xcor()-t2.xcor(),2)+math.pow(t1.ycor()-t2.ycor(),2))
    return(distance < 15)
 
game_is_on = True

while game_is_on:

    screen.update()
    time.sleep(0.01)

    #Move the bullet
    if bullet.state == "fire":
        bullet.move()

    #Check to see if the bullet has gone to the top
    if bullet.ycor() > 270:
        bullet.reset()

    for enemy in enemies.enemies:
        #Move the enemy
        enemy.move()
        #Move the enemy back and down
        if enemy.xcor() > 370 or enemy.xcor() < -380:
            #Move all the enemies down and change direction
            for e in enemies.enemies:
                e.move_down()
                e.move_speed *= -1
        #Check for collision between bullet and enemy
        if isCollision(bullet, enemy):
            score.increase_score()
            enemies.destroy_enemy(enemy)
            bullet.reset()
            break
        if enemy.ycor() < -280:
            bullet.reset()
            score.reset()
            game_is_on = False
            print("Game Over")
            break

    # detect level-up
    if len(enemies.enemies) == 0:
        screen.update()
        score.next_level()
        enemies = Enemies(score.level)


screen.exitonclick()
