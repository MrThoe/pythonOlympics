import turtle as t
from random import randint 

sven = t.Turtle()
sven.speed(0)

wn = t.Screen()
wn.colormode(255)
sven.shape('turtle')

def distance(x, y):
    d = ((x**2)+(y**2))**(1/2)
    return d

for i in range(10000):
    x = randint(-400, 400)
    y = randint(-400, 400)
    sven.pu()
    sven.goto(x,y)
    d = distance(x,y)
    if d > 200:
        r = 197
        b = 88
        g = 179
    else:
        r = 0
        b = 0
        g = 0
    sven.color(r,g,b)
    sven.stamp()
