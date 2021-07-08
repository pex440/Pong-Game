import turtle
from Entity import Entity #the pen is an invisible entity
class Pen(Entity): 
    def __init__(self,screen):
        super().__init__(screen)
        self.t.hideturtle() # making the pen invisible
        self.t.goto(0, screen.h//2-40) #going to the top of the screen
        self.t.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal")) #Writing a basic score

    def updateScore(self,score1,score2,pointsToAdd=1):
        self.t.clear() #removing all the pen writes
        self.t.write("Player A: {}  Player B: {}".format(score1, score2), align="center", font=("Courier", 24, "normal")) #re-writing the updated score
        