from turtle import Turtle
import random
import time

FONT = ('Courier', 52, 'normal')
ALIGNMENT = 'center'
COLOR_LIST = ['light blue', 'royal blue',
		'light steel blue', 'steel blue',
		'light cyan', 'light sky blue',
		'violet', 'salmon', 'tomato',
		'sandy brown', 'purple', 'deep pink',
		'medium sea green', 'khaki']


class UI(Turtle):
	def __init__(self):
		super().__init__()
		self.hideturtle()
		self.penup()
		self.color(random.choice(COLOR_LIST))
		self.header()

	def header(self):
		self.clear()
		self.goto(x=0, y=-150)
		self.write('Breakout', align=ALIGNMENT, font=FONT)

	def change_color(self):
		self.clear()
		self.color(random.choice(COLOR_LIST))
		self.header()

	def game_over(self, win):
		self.clear()
		if win == True:
			self.write('YOU WIN!', align='center', font=FONT)
		else:
			self.write('Game is Over', align='center', font=FONT)
