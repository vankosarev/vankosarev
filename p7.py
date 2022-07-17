import turtle

class L:
    def __init__(self, t, axiom, width, lengthF, angle):
        self.axiom = axiom
        self.state = axiom
        self.width = width
        self.lengthF = lengthF
        self.angle = angle
        self.t = t
        self.rules = {}
        self.t.pensize(self.width)
        

    def add_rules(self,*rules):
        for key, value in rules:
            self.rules[key] = value
            
    def generate_path(self, n_iter):
        for me in range(n_iter):
            for key, value in self.rules.items():
                self.state = self.state.replace(key,value.lower())

                self.state = self.state.upper()

    def draw_turtle(self, start_pos, start_angle):
        turtle.tracer(2,0)
        self.t.up()
        self.t.setpos(start_pos)
        self.t.seth(start_angle)
        self.t.down()

        for move in self.state:
            if move == 'F':
                self.t.forward(self.lengthF)
            elif move == '+':
                self.t.left(self.angle)
            elif move == '-':
                self.t.right(self.angle)

        turtle.done()
            

width = 1920
height = 1080
screen = turtle.Screen()
screen.setup(width, height, 0,0)

t = turtle.Turtle()
t.ht()

pen_width = 2
f_len = 3
angle = 60
axiom = "F+F+F+F+F+F"


l_sys = L(t,axiom, pen_width, f_len, angle)
l_sys.add_rules(("F", "F+FF--FF+F"))
l_sys.generate_path(3)
l_sys.draw_turtle((0,0),0)

        



