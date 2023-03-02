from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from bricks import Bricks
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

paddle = Paddle()
bricks = Bricks()
ball = Ball()
 
screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)
 
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.03)
    ball.move()

    # record x-axis coordinates of ball and paddle
    paddle_x = paddle.xcor()
    ball_x = ball.xcor()
    ball_y = ball.ycor()
 
    # detect collision with left and right walls:
    if ball_x < -380 or ball_x > 370:
        ball.bounce(True, False)
 
    # detect collision with upper wall
    elif ball_y > 270:
        ball.bounce(False, True)
 
    # detect collision with bottom wall
    # In this case, user failed to hit the ball
    # thus he loses. The game resets.
    elif ball_y < -280:
        ball.reset()

    # check if ball's distance(from its middle)
    # from paddle(from its middle) is less than
    # width of paddle and ball is below a certain
    # coordinate to detect their collision
    elif ball.distance(paddle) < 110 and ball_y < -250:
 
        # If Paddle is on Right of Screen
        if paddle_x > 0:
            if ball_x > paddle_x:
                # If ball hits paddles left side it
                # should go back to left
                ball.bounce(True, True)
            else:
                ball.bounce(False, True)
 
        # If Paddle is left of Screen
        elif paddle_x < 0:
            if ball_x < paddle_x:
                # If ball hits paddles left side it
                # should go back to left
                ball.bounce(True, True)
            else:
                ball.bounce(False, True)
 
        # Else Paddle is in the Middle horizontally
        else:
            if ball_x > paddle_x:
                ball.bounce(True, True)
            elif ball_x < paddle_x:
                ball.bounce(True, True)
            else:
                ball.bounce(False, True)

screen.exitonclick()