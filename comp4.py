import turtle

sven = turtle.Turtle()
sven.left(180)

sven2 = turtle.Turtle()
sven2.left(180)
sven2.color("Green")

bill = turtle.Turtle()
bill.color("RED")

bill2 = turtle.Turtle()
bill2.color("YELLOW")

def square(n, anyTurtle):
      for i in range(4):
            anyTurtle.forward(n)
            anyTurtle.right(90)
sven.shape("turtle")            
sven.begin_fill()    #Start of shape         
square(50, sven)
sven.end_fill()      #End of your shape


sven2.shape("turtle")
sven2.right(90)
sven2.begin_fill()    #Start of shape         
square(300, sven2)
sven2.end_fill() 


bill.shape("circle")
bill.begin_fill()
square(100, bill)
bill.end_fill()

bill2.shape("circle")
bill2.left(90)
bill2.begin_fill()
square(200, bill2)
bill2.end_fill()            
