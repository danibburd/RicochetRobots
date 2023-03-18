import board

#Robot class to store x and y position
class robot:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def setX(self, newX):
        self.x = newX

    def setY(self, newY):
        self.y = newY

    def getX(self):
        return self.x
    
    def getY(self):
        return self.y

#define a board and robots
gameBoard = board([14,7])
robot1 = robot(2,13)



#checks a row/column for position to stop in
def makeMove():
    #determine whether going up/down
    #get x/y
    #go incrementally from robot position until a wall or robot is found
    #check for goals reached
    #move robot to that position
    return

#Checks for any collisions in the way 
