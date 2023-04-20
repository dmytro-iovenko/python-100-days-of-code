from turtle import Turtle

class Scoreboard(Turtle):

    def __init__(self, level):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.level = level
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score} | Level: {self.level}", 
                   align="center", font=("Courier", 18, "normal"))

    def increase_score(self):
        self.score += 1
        self.update_score()
 
    def next_level(self):
        self.level += 1
        self.update_score()
 
    def reset(self):
        self.clear()
        self.score = 0
        self.update_score()
