import cTurtle
import math

class Planet:
    def __init__(self, iname, irad, im, idist, ivx, ivy, ic, inumMoons, imoonList):
        self.name = iname
        self.radius = irad
        self.mass = im
        self.distance = idist
        self.x = idist
        self.y = 0
        self.color = ic
        self.velx = ivx
        self.vely = ivy
        self.numMoons = inumMoons
        self.moonList = imoonList
        
        self.pturtle = cTurtle.Turtle()
        
        self.pturtle.color(self.color)
        self.pturtle.shape("circle")
        self.pturtle.resizemode("user")
        self.pturtle.turtlesize(self.radius/300, 0)
        
        self.pturtle.up()                    
        self.pturtle.goto(self.x,self.y)     
        self.pturtle.down()                
    
    def moveTo(self, newx, newy):
    	self.x = newx
    	self.y = newy
    	self.pturtle.goto(newx, newy)
    	
    def getXVel(self):
    	return self.velx
    
    def getYVel(self):
    	return self.vely
    
    def getName(self):
        return self.name
    
    def getRadius(self):
        return self.radius
    
    def getMass(self):
        return self.mass
    
    def getDistance(self):
        return self.distance
        
    def getnumMoons(self):
    	return self.numMoons
    
    def getVolume(self):
        v = 4.0/3 * math.pi * self.radius**3
        return v
    
    def getSurfaceArea(self):
        sa = 4.0 * math.pi * self.radius**2
        return sa
    
    def getDensity(self):
        d = self.mass / self.getVolume()
        return d
        
	def getCircumference(self):
		c = 2.0 * math.pi * self.radius
		return c
    
    def setName(self, newname):
        self.name = newname
        
    def setXVel(self, newvx):
    	self.velx = newvx
    	
    def setYVel(self, newvy):
    	self.vely = newvy
        
    def setMoons(self, newmoons):
    	self.numMoons = newmoons
    	
    def addMoon(self, newmoon):
    	self.moonList.append(newmoon)
    
    def show(self):
        print(self.name)
    
    def __str__(self):
        return self.name
    
    def getXPos(self):
        return self.x
    
    def getYPos(self):
        return self.y