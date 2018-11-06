import turtle

sven = turtle.Turtle()
sven.speed(2)

def circ(r):
    sven.pu()
    sven.setheading(270)
    sven.forward(r)
    sven.pd()
    sven.setheading(0)
    sven.circle(r)
    sven.pu()
    sven.setheading(270)
    sven.forward(-r)

sven.setheading(210)
sven.pu()
sven.forward(50 * (3**(1/2)))

for i in range (3):
    sven.setheading(120*i)
    sven.pu()
    sven.forward(200)
    sven.pd()
    sven.begin_fill()
    circ(100)
    sven.end_fill()
    
sven.pu()
sven.goto(0,0)

    
