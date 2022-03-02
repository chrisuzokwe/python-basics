import math


class SodaCan:
    def __init__(self, height, radius):
        self.height = height
        self.radius = radius

    def getsurfacearea(self):
        return (self.height*math.pi*2.0*self.radius) + (2*math.pi*self.radius**2)

    def getvolume(self):
        return math.pi*self.height*(self.radius**2)


sprite = SodaCan(5, 6)
SurfaceArea = sprite.getsurfacearea()
Volume = sprite.getvolume()
print SurfaceArea, Volume
