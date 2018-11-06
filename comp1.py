import turtle
from random import *

sven = turtle.Turtle()

### If you want to use Colormode you must create a turtle.Screen() method
wn = turtle.Screen()
wn.colormode(255)

sven.color(255,255,255)  #White
wn.bgcolor(0,0,0)  #Black

def drawSq(n):
      #n = 100
      sven.pu()
      sven.goto(-n/2, n/2)
      sven.pd()
      for i in range(4):
            sven.forward(n)
            sven.right(90)

drawSq(100)
