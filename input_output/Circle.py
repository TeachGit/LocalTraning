import math
from GeometricObject import GeometricObject


class Circle(GeometricObject):
    def __init__(self, radius):
        super().__init__()
        self.__radius = radius

    def getRadius(self):
        return self.__radius

    def setRadius(self, radius):
        self.__radius = radius

    def getDiameter(self):
        return 2 * self.__radius

    def getPerimeter(self):
        return 2 * math.pi * self.__radius

    def getArea(self):
        return math.pi * self.__radius * self.__radius

    def printCircle(self):
        return self.__str__() + " Radius :" + str(self.__radius)
