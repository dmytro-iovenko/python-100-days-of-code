from turtle import Turtle
 
MOVE_DIST = 15
 
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("player.gif")
        #self.shape("square")
        #self.color("blue")
        #self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.goto(x=0, y=-250)
 
    def move_left(self):
        x = self.xcor()
        if x > -280:
            self.backward(MOVE_DIST)
 
    def move_right(self):
        x = self.xcor()
        if x < 280:
            self.forward(MOVE_DIST)