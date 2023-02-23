from turtle import*
import random

'''
FUNCTIONS AND CLASS DEFINITIONS 
'''
def random_color():
	color="#"
	symbols="0123456789ABCDEF"
	for i in range(6):
		index=random.randint(0,15)
		color+=symbols[index]
	return color
  
def border():
	b=Turtle()
	b.speed(0)
	b.ht()
	b.pu()
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

class Falling_Object(Turtle):
  def __init__(self):
    super().__init__()
    self.shape=random.choice(["circle, square"])
    self.speed=0
    self.color=random_color()
    x=random.randint(-150,150)
    y=random.randint(200,300)
    self.goto(x,y)
  
  def move(self):
    self.seth(270)
    self.forward(10)

class Player:
	def __init__(self):
		self.shape="turtle"
		self.speed=0
		self.color=random_color()

  #def move_
	
####### PROGRAM #############
# Creates screen object

"""
PROGRAM
"""

############ SCREEN ############
screen=Screen()
screen.bgcolor("black")
# the listen function notifies the program that it will need to be paying attention to inputs(key presses) from the user.
screen.listen()

############ BORDER ##########
border()

########## GAME LOOP #########
falling_objects=[]
for i in range(10):
  object=Falling_Object()
  falling_objects.append(object)

while True:
  for object in falling_objects:
    object.move
