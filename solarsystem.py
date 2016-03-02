import cTurtle
import math

class SolarSystem:
    
    def __init__(self, width, height):
        self.thesun = None
        self.planets = []
        self.ssturtle = cTurtle.Turtle()   
        self.ssturtle.hideturtle()
        self.ssturtle.setWorldCoordinates(-width/2.0, -height/2.0,
                                           width/2.0,  height/2.0)   
    
    def addPlanet(self, aplanet):
        self.planets.append(aplanet)
        
    def addSun(self, asun):  
        self.thesun = asun   
        
    def showPlanets(self):
        for aplanet in self.planets:
            print(aplanet) # bug fixed: Listing 10.9 missed the parentheses
            
    def movePlanets(self):
    
    	G = .1
    	dt = .001
    	
    	for p in self.planets:
    		p.moveTo(p.getXPos() + dt * p.getXVel(),
    				p.getYPos() + dt * p.getYVel())
    				
    		rx =self.thesun.getXPos() = p.getXPos()
            ry =self.thesun.getYPos() = p.getYPos()
            r = math.sqrt(rx**2 + ry**2)
            
            accx = G * self.thesun.getMass()*rx/r**3
            accy = G * self.thesun.getMass()*ry/r**3
            
            p.setXVel(p.getXVel() + dt * accx)
            p.setYVel(p.getYVel() + dt * accy)
            
    def freeze(self):                
        self.ssturtle.exitOnClick()
        
    def numPlanets(self):
    	return len(self.planets)
    	
    def totalMass(self):
		total_mass = 0
			for aplanet in self.planets:
        		total_mass = total_mass + aplanet.getMass()
    return total_mass
    
    def removePlanet(self, aplanet):
    	if aplanet in self.planets: self.planets.remove(aplanet)
    	
    def getNearest(self):
    	dist = sorted(self.planets, key=lambda aplanet: aplanet.distance)
    	return dist[0]
    	
    def getFarthest(self):
    	dist = sorted(self.planets, key=lambda aplanet: aplanet.distance)
    	return dist[-1]
    	
    def __str__(self):
    	print self.thesun.name
    	self.planets = sorted(self.planets, key=lambda aplanet: aplanet.distance)
    	self.showPlanets()
    	