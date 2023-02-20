import turtle, time
from random import randint as r

'''
FUNCTIONS AND CLASS DEFINITIONS 
'''
class Falling_Object:
	def __init__(self, shape, speed, color):
		self.shape = shape
		self.speed = speed
		self.color = color

	#def move():

class Player:
	def __init__(self, shape, speed, color):
		self.shape = shape
		self.speed = speed
		self.color = color
	
def border():
	b = turtle.Turtle()
	b.speed(0)
	b.ht()
	b.bu()
	b.width(10)
	b.color("white")
	b.goto(-110,200)
	b.pendown()
	b.begin_fill()
	for i in range(2):
		b.forward(220)
		b.right(90)
		b.forward(400)
		b.right(90)
	b.end_fill()
	
	
	####### PROGRAM #############
	# Creates screen object
	
	"""
	PROGRAM
	"""
	
	############ SCREEN ############
	screen = turtle.Screen()
	screen.bgcolor("black")
	# the listen function notifies the program that it will need to be paying attention to inputs(key presses) from the user.
	screen.listen()
	
	############ BORDER ##########
	border()
	
	########## GAME LOOP #########