import turtle
from Paddle import Paddle
from Entity import Entity
from Ball import Ball
from Pen import Pen
class MyScreen:   
    def __init__(self, w=1024, h=576,ballspeed = 0.5, title ='Pong-Game by pex440',bgcolor='black'): 
        self.wn = turtle.Screen() #self.wn is the screen object 
        self.wn.title(title)      #setting the title
        self.wn.bgcolor(bgcolor)  #setting the background
        self.w = w                #screen width 
        self.h = h                #screen height
        self.ballspeed = ballspeed
        self.wn.setup(width = self.w, height=self.h) #setting the screen in width and height
        self.wn.tracer(0) #Turns turtle animation off 

    def mainLoop(self):
        pen = Pen(self) #Creating a pen to write the score on the Screen
        p1 = Paddle(self,'l') #creating the first paddle
        p2 = Paddle(self,'r') #creating the second paddle
        ball = Ball(self,self.ballspeed)#creating a ball
        
        while True:
            self.wn.update() #updating the screen 
            self.wn.listen() #letting the screen listen to user commands
            ball.move(p1,p2,pen) #The method that makes the ball move, also it keeps and writes the score

             #left paddle movement
            self.wn.onkeypress(p1.goUp,'w')
            self.wn.onkeypress(p1.goUp,'W')
            self.wn.onkeypress(p1.goDown,'s')
            self.wn.onkeypress(p1.goDown,'S')

             #right paddle movement
            self.wn.onkeypress(p2.goDown,'Down')
            self.wn.onkeypress(p2.goUp,'Up')


if __name__ == '__main__':
    screen = MyScreen()
    screen.mainLoop()


