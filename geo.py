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

    def getArea(self):
        a = math.pi * self.r * self.r
        return a

class RightAngleTriangle:


    def setSides(self, right, left):
        self.r = right
        self.l = left
        if (self.r == 0 or self.l == 0 or self.r > self.getLongSide() or self.l > self.getLongSide()):
            raise ArithmeticError("the two sides must be less long than the longest side and greater than 0 length")

    def getLongSide(self):

        ls = (self.r * self.r) + (self.l * self.l)
        return math.sqrt(ls)

    def getLeftOppositeAngle(self):

        lsacos = (self.getLongSide() * self.getLongSide() + self.l * self.l - self.r * self.r) / (2 * self.getLongSide() *self.l)
        lsa = math.acos(lsacos) * 180 / math.pi
        return lsa

    def getRightOppositeAngle(self):

        rsacos = (self.getLongSide() * self.getLongSide() + self.r * self.r - self.l * self.l) / (2 * self.getLongSide() * self.l)
        rsa = math.acos(rsacos) * 180 / math.pi
        return rsa



if __name__ == '__main__':

    
    c =  Circle()
    print("asserting radius ", 8)
    c.setRadius(8)
    print("circumference is ", c.getCirc())
    print("area is", c.getArea())
    print("asserting sides 5 and 5")
    r = RightAngleTriangle()
    r.setSides(5, 5)
    s = r.getLongSide()
    print("longest side is ", r.getLongSide())
    print("right opposite angle is:")
    print(r.getRightOppositeAngle(), "degrees")

    assert c.getArea() > 201, "two sides must be less long than the longest side and greater than 0 length"

