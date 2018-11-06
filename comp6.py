import turtle
import random

sven = turtle.Turtle()
AnyName = ["Blue" , "Green", "Yellow" , "Red" , "Black"]  #LIST of random colors
sven.speed(7)
sven.pensize(3)
# Draw a square
# Select all, Hold CTR + TAB

def Square(s):          #Add a variable to make it more ABSTRACT
    for i in range(5):
        num = random.randint(0,4)
        sven.color(AnyName[num])
        sven.forward(s)
        sven.right(72)



for n in range(100):
    sven.pu()   #Picks up the pen
    sven.goto(-5 * n, 5 * n)
    sven.pd()   #Puts the pen down
    
    Square (10 * n)

