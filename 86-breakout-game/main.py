from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
ball = Ball()
 
screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)
 
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.03)
    ball.move()

    # detect collision with left and right walls:
    if ball.xcor() < -380 or ball.xcor() > 370:
        ball.bounce(x_bounce=True, y_bounce=False)
 
    # detect collision with upper wall
    elif ball.ycor() > 270:
        ball.bounce(x_bounce=False, y_bounce=True)
 
    # detect collision with bottom wall
    # In this case, user failed to hit the ball
    # thus he loses. The game resets.
    elif ball.ycor() < -280:
        ball.reset()

screen.exitonclick()