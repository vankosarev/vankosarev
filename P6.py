import turtle

width = 1200
height = 600
screen = turtle.Screen()
screen.setup(width,height,0,0)


def draw_koch_segment(x,ln):
    if ln > 6:
        ln3 = ln // 3
        draw_koch_segment(t, ln3)
        t.left(60)
        draw_koch_segment(t, ln3)
        t.right(120)
        draw_koch_segment(t, ln3)
        t.left(60)
        draw_koch_segment(t, ln3)
    else:
        t.fd(ln)
        t.left(60)
        t.fd(ln)
        t.right(120)
        t.fd(ln)
        t.left(60)
        t.fd(ln)
    
    

t = turtle.Turtle()
t.speed(10)
draw_koch_segment(t, 150)
t.right(120)
draw_koch_segment(t, 150)
t.right(120)
draw_koch_segment(t, 150)


turtle.done()  

        
    





    
