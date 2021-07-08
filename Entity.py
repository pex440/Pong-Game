import turtle
class Entity:
    def __init__(self,screen,speed=0,shape='square',color = 'white'):
        self.screen = screen # the screen value is turle.Screen()
        self.t = turtle.Turtle() # this is the self turtle property, the turtle.Turtle() object
        self.t.speed(speed) # Here i set the drawing speed, usually 0, the maximum so at the game start all the objects are already drawn
        self.t.shape(shape) # This is the shape of the turtle.Turtle() object
        self.t.color(color) # This is the color of the turtle.Turtle() object
        self.t.penup()      # without leaving the pen there would be a line of the path made by the game object since these are drawn starting from the center
        self.t.goto(0,0)    # Here I set the initial position of turtle.Turtle() object