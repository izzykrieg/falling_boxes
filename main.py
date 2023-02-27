from turtle import*
import random

'''
FUNCTIONS AND CLASS DEFINITIONS 
'''
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
    self.hideturtle()
    self.pu()
    self.speed(0)
    self.shape(random.choice(["circle", "square", "triangle"]))
    self.color(random.choice(["orange", "pink", "yellow"]))
    x=random.randint(-150,150)
    y=random.randint(200,600)
    self.goto(x,y)
    self.seth(270)
  
  def move(self):
    self.forward(10)
    if self.ycor()>-195 and self.xcor()>-105 and self.ycor()<195 and self.xcor()<105:
      self.showturtle()
    if self.ycor()<-195:
      x=random.randint(-150,150)
      y=random.randint(200,600)
      self.goto(x,y)

class Player(Turtle):
  def __init__(self):
    super().__init__()
    self.speed(0)
    self.shape("turtle")
    self.color("light green")
    self.goto(0,-180)
    self.pu()

  def move_left(self):
    if self.xcor()>-105:
      self.setx(self.xcor()-5)

  def move_right(self):
    if self.xcor()<95:
      self.setx(self.xcor()+5)
  
####### PROGRAM #############
# Creates screen object

"""
PROGRAM
"""

############ SCREEN ############
player=Player()
screen=Screen()
screen.bgcolor("black")
# the listen function notifies the program that it will need to be paying attention to inputs(key presses) from the user.
screen.listen()
screen.onkeypress(player.move_left,"Left")
screen.onkeypress(player.move_right,"Right")

############ BORDER ##########
border()
########## GAME LOOP #########

falling_objects=[]
for i in range(10):
  object=Falling_Object()
  falling_objects.append(object)

#score_objects=[]
#score = 0
while True:
 for object in falling_objects:
  object.move()
  if object.ycor()<-195 or object.ycor()>195 or object.xcor()>105 or object.xcor()<-105:
    object.hideturtle()
    #object.write(str(object.pos()))
  #if object.ycor()<-195 and object.ycor()>195 and object.xcor()>105 and object.xcor()<-105:
  #  score_objects.append(object)
    
  if player.distance(object)<20:
    player.hideturtle()
  #  for object in score_objects:
  #    if object.ycor()<-195:
  #      score += 1
  #break
