import turtle

turtle.pendown
turtle.speed(100)



n = int(input("кол-во:"))

def p(n):
    for i in range(n):
        turtle.forward(100)
        turtle.left(360/n)





for f in range(0,n):
    p(n)
    turtle.left(360/n)
    turtle.forward(100)



