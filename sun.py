import cTurtle

class Sun:
    def __init__(self, iname, irad, im, itemp):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.temp = itemp
        self.x = 0
        self.y = 0
        
        self.sturtle = cTurtle.Turtle()
        self.sturtle.shape("circle")
        self.sturtle.color("yellow")
    
    def getMass(self):
        return self.mass
    
    def __str__(self):
        return self.name
    
    def getXPos(self):
        return self.x
    
    def getYPos(self):
        return self.y