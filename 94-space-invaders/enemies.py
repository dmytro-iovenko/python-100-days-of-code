from turtle import Turtle
import random

 
class Enemy(Turtle):
    def __init__(self, x_cor, y_cor, level):
        super().__init__()
        self.penup()
        self.shape("square")
        self.color("red")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.goto(x=x_cor, y=y_cor)
        self.move_speed = level + 1
        self.speed(0)
  
    def move(self):
        new_x = self.xcor() + self.move_speed
        self.goto(new_x, self.ycor())

    def move_down(self):
        new_y = self.ycor() - 30
        self.goto(self.xcor(), new_y)

class Enemies:
    def __init__(self, level):
        self.y_start = 0
        self.y_end = 240
        self.difficulty = level
        self.number_of_enemies = 4 + self.difficulty
        self.enemies = []
        self.create_enemies()
 
    def create_enemies(self):
        for i in range(self.number_of_enemies):
            x = random.randint(-200,200)
            y = random.randint(100,250)
            enemy = Enemy(x, y, self.difficulty)
            self.enemies.append(enemy)
 
    def destroy_enemy(self, enemy):
        enemy.clear()
        enemy.goto(3000, 3000)
        self.enemies.remove(enemy)
