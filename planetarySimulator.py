from solarsystem import *
from sun import *
from planet import *

def createSS():
    ss = SolarSystem(2,2)
    ss.addSun(Sun("SUN", 5000, 10, 5800))
    ss.addPlanet(Planet("MERCURY", 19.5, 1000, .25, 0, 2, 'blue', 0, []))
    ss.addPlanet(Planet("EARTH", 47.5, 5000, .3, 0, 2.0, 'green', 0, []))
    ss.addPlanet(Planet("MARS", 50, 9000, .5, 0, 1.63, 'red', 0, []))
    ss.addPlanet(Planet("JUPITER", 100, 49000, .7, 0, 1, 'black', 0, []))
    ss.addPlanet(Planet("SATURN", 58, 15000, .9, 0, 1.3, 'brown', 0, []))
    return ss