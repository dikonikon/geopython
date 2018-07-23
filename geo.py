import math

class Circle:

    def __init__(self):
        self.r = 0

    def setRadius(self, radius):
        self.r = radius
        return self.r

    def getCirc(self):
        c = 2 * math.pi * self.r
        return c

if __name__ == '__main__':

    
    c =  Circle()
    print("asserting radius ", 8)
    c.setRadius(8)
    print("circumference is ", c.getCirc())