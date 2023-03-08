from turtle import Turtle

try:
    score = int(open('highscore.txt', 'r').read())
except FileNotFoundError:
    score = open('highscore.txt', 'w').write(str(0))
except ValueError:
    score = 0

class Scoreboard(Turtle):

    def __init__(self, lives):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.highScore = score
        self.lives = lives
        self.score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(0, 260)
        self.write(f"Score: {self.score} | Highest Score: {self.highScore} | Lives: {self.lives}", 
                   align="center", font=("Courier", 18, "normal"))

    def increase_score(self):
        self.score += 1
        if self.score > self.highScore:
            self.highScore += 1
        self.update_score()
 
    def decrease_lives(self):
        self.lives -= 1
        self.update_score()
 
    def reset(self):
        self.clear()
        self.score = 0
        self.update_score()
        open('highscore.txt', 'w').write(str(self.highScore))
