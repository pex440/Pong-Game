from Entity import Entity

class Paddle(Entity):   # the paddle is a child of the Entity class
    def __init__(self,screen,side,step = 50):
        
        super().__init__(screen)    
        self.score = 0
        self.t.shapesize(stretch_wid=5,stretch_len=1) #since the entity is a paddle, it needs to be stretched vertically to be changed from a square to a rect   
        self.step = step

        self.side = side.lower() #since this is a pong game, a paddle can just be on the left or on the right 
        if self.side == 'l':side = -1 
        elif self.side == 'r':side = 1
        else: raise ValueError("Side values can only be \'l\' or \'r\' (Lower or Upper)")  # The side values can only be 'l' or 'r' 
    
        self.t.goto(side*(screen.w/2-self.step),0) #50 pixels from the left border #screen_width/2-50 #the initial position of the paddle
    
    # This are two methods for the Paddle movement, since it is pong, the Paddles can only move vertically 
    # Y coordinate incremented or decremented by the self.step value
    def goUp(self): 
        if self.t.ycor()<self.screen.h/2-self.step: #clamp, the maximum player height is 250, so height/2-step
            self.t.sety(self.t.ycor()+self.step)
            
    
    def goDown(self):
        if self.t.ycor()>-(self.screen.h/2-self.step): #clamp, the minimum player height is -250, so -(height/2-step)
            self.t.sety(self.t.ycor()-self.step)