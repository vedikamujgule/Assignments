# (Geometry: intersection) Suppose two line segments intersect. The two endpoints
# for the first line segment are (x1, y1) and (x2, y2) and for the second line segment
# are (x3, y3) and (x4, y4). Write a program that prompts the user to enter these
# four endpoints and displays the intersecting point. (Hint: Use the
# LinearEquation class from Exercise 7.7.)

class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    def getA(self):
        return self.__a

    def getB(self):
        return self.__b

    def getC(self):
        return self.__c

    def getD(self):
        return self.__d

    def getE(self):
        return self.__e

    def getF(self):
        return self.__f

    def isSolvable(self):
        d = self.__a * self.__d - self.__b * self.__c
        return True if d != 0 else False

    def getX(self):
        d = self.__a * self.__d - self.__b * self.__c
        n = self.__e * self.__d - self.__b * self.__f
        return n / d

    def getY(self):
        d = self.__a * self.__d - self.__b * self.__c
        n = self.__a * self.__f - self.__e * self.__c
        return n / d
    
x1, y1, x2, y2 = eval(input("Enter the endpoints (x1, y1, x2, y2) of the 1st line segment: "))
x3, y3, x4, y4 = eval(input("Enter the endpoints (x3, y3, x4, y4) of the 2nd line segment: "))

a = y1 - y2
b = -x1 + x2
c = y3 - y4
d = -x3 + x4
e = -y1 * (x1 - x2) + (y1 - y2) * x1
f = -y3 * (x3 - x4) + (y3 - y4) * x3

eq = LinearEquation(a, b, c, d, e, f)
print("The intersecting point is: (", eq.getX(), ",", eq.getY(), ")")