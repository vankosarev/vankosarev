import turtle
import math 


def polygon(nangle,lenght):
    a = 360/nangle

    for i in range(0,nangle):
        turtle.forward(lenght)
        turtle.left(a)
        
    
def star(nray,lenght):
    a = 360/nray
    b = 360/(nray/2)
    for i in range(0,nray):
        turtle.forward(lenght)
        turtle.right(b)
        turtle.forward(lenght)
        turtle.left(a)
        
def circle(rad):
    
    for i in range(0,360):
        turtle.forward(2)
        turtle.left(1)

circle(50)
    
