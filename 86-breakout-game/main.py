from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from bricks import Bricks
from scoreboard import Scoreboard
from ui import UI
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Breakout")
screen.tracer(0)

ui = UI()
ui.header()

score = Scoreboard(lives=5)
paddle = Paddle()
bricks = Bricks()
ball = Ball()
 
screen.listen()
screen.onkey(key='Left', fun=paddle.move_left)
screen.onkey(key='Right', fun=paddle.move_right)
 
game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.01)
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
        score.decrease_lives()
        if score.lives == 0:
            score.reset()
            ui.game_over(win=False)
            break
        ui.change_color()

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

    for brick in bricks.bricks:
        if (ball_x + 25 > brick.left_wall and 
            ball_x - 25 < brick.right_wall and 
            ball_y + 15 > brick.bottom_wall and 
            ball_y - 15 < brick.upper_wall):

            # detect collision from left
            if ball_x < brick.left_wall:
                ball.bounce(True, False)
 
            # detect collision from right
            elif ball_x > brick.right_wall:
                ball.bounce(True, False)
 
            # detect collision from bottom
            elif ball_y < brick.bottom_wall:
                ball.bounce(False, True)
 
            # detect collision from top
            elif ball_y > brick.upper_wall:
                ball.bounce(False, True)
 
            score.increase_score()
            brick.quantity -= 1
            if brick.quantity == 0:
                brick.clear()
                brick.goto(3000, 3000)
                bricks.bricks.remove(brick)

    # detect victory
    if len(bricks.bricks) == 0:
        ui.game_over(win=True)
        break

screen.exitonclick()