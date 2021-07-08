from Entity import Entity

class Ball(Entity): #this ball is a child of the Entity class 
    def __init__(self,screen,speed):
        super().__init__(screen,shape='circle')
        #ball speed
        self.t.dx = speed 
        self.t.dy = speed
        
        #ball screen limits
        self.w_limit = self.screen.w/2-10 
        self.h_limit = self.screen.h/2-10
    
    #ball movement
    def move(self,p1,p2,pen):
        #making the ball move by adding her xcor and ycor dx and dy
        self.t.setx(self.t.xcor() + self.t.dx)
        self.t.sety(self.t.ycor() + self.t.dy)
        #making the ball stay inside the screen
        self.clamp(p1,p2,pen)
        #making the ball bounce when it hits the player
        self.detectPlayerCollision(p1,p2)

    #boolean return functions for ball collisions with the borders
    def leftBorderCollision(self):
        if self.t.xcor()<-self.w_limit:
            return True
        else:return False
        
    def rightBorderCollision(self):
        if self.t.xcor()>self.w_limit:
            return True
        else:return False

    def topBorderCollision(self):
        if self.t.ycor()>self.h_limit:
            return True
        else: return False
    def bottomBorderCollision(self):
        if self.t.ycor()<-self.h_limit:
            return True
        else:return False

    #function to make the ball bounce at the player collision
    def detectPlayerCollision(self,p1,p2):
            p_xcor = abs(int(p1.t.xcor())) # for a screen width of 800 it should be 800/2-paddle_step. I need it to clamp the ball on the x axis, then I get the ycor for the y axis
            
            if self.t.xcor()>p_xcor-10 and (self.t.ycor()< p2.t.ycor() +p2.step and self.t.ycor() > p2.t.ycor() -p2.step):
                self.t.setx(p_xcor-10)
                self.t.dx *= -1 #this changes the ball's verse

            if self.t.xcor()<-(p_xcor-10) and (self.t.ycor()< p1.t.ycor() +p1.step and self.t.ycor() > p1.t.ycor() -p1.step):
                self.t.setx(-(p_xcor-10))
                self.t.dx *= -1 #this changes the ball's verse
    
    #function to make the ball bounce on the borders and going to the centre if it touches left or right border
    #also it keeps the score
    def clamp(self,p1,p2,pen):
        if self.topBorderCollision():
            self.t.sety(self.h_limit)
            self.t.dy *= -1 

        if self.bottomBorderCollision():
            self.t.sety(-self.h_limit)
            self.t.dy *= -1 
        
        if self.rightBorderCollision():
            self.t.setx(self.w_limit)
            self.t.dx *= -1
            self.t.goto(0,0)
            p1.score+=1
            
        if self.leftBorderCollision():
            self.t.setx(-self.w_limit)
            self.t.dx *= -1
            self.t.goto(0,0)
            p2.score+=1

        pen.updateScore(p1.score,p2.score) #updating the score on the screen
            
            
            