import math

class Point:
    def __init__(self, x=0, y=0):
        self.__x__ = x
        self.__y__ = y

    def getX(self):
        return self.__x__

    def getY(self):
        return self.__y__

    def distance(self, point):
        dis = math.sqrt((self.__x__ - point.getX()) ** 2 + (self.__y__ - point.getY()) ** 2)
        return dis

    def isNearBy(self, point):
        d = self.distance(point)
        return True if d < 5 else False

    def _str_(self):
        return '( ' + str(self.__x__) + ',' + str(self.__y__) + ' )'

def main():
    x1, y1, x2, y2 = eval(input("Enter two points x1, y1, x2, y2: "))
    p1 = Point(x1, y1)
    p2 = Point(x2, y2)
    print("The distance between the two points is", p1.distance(p2))
    if p1.isNearBy(p2):
        print("The two points are near each other")
    else:
        print("The two points are not near each other")
main()