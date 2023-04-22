from turtle import Turtle

BULLET_SPEED = 10

class Bullet(Turtle):

    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("triangle")
        self.penup()
        self.y_move = BULLET_SPEED
        self.setheading(90)
        self.shapesize(0.5, 0.5)
        self.reset()

    def move(self):
        new_y = self.ycor() + self.y_move
        self.goto(self.xcor(), new_y)

    def fire(self, player):
        if self.state == "ready":
            self.state = "fire"
            #Move the bullet to above the player
            self.setposition(player.xcor(), player.ycor()+10)
            self.showturtle()

    def reset(self):
        self.hideturtle()
        self.goto(3000, 3000)
        self.state = "ready"
