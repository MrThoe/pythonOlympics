import turtle
from random import *

sven = turtle.Turtle()
sven.speed(9)
p = 1

### If you want to use Colormode you must create a turtle.Screen() method
wn = turtle.Screen()
wn.colormode(255)

sven.color(255,255,0)  #Yellow
wn.bgcolor(0,0,255)  #Blue

def drawSq(n):
      #n = 100
      sven.pu()
      sven.goto(-n/2, n/2)
      sven.pd()
      for i in range(4):
            sven.forward(n)
            sven.right(90)
for i in range(30):
      sven.pensize(p)
      drawSq(24 * i + 12)
      if (i%5 == 0):
            p = p + 1
