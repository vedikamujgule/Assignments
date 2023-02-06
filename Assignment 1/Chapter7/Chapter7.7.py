# (Algebra: linear equations) Design a class named LinearEquation for a
# system of linear equations:
# The class contains:
# ■ The private data fields a, b, c, d, e, and f with get methods.
# ■ A constructor with the arguments for a, b, c, d, e, and f.
# ■ Six get methods for a, b, c, d, e, and f.
# ■ A method named isSolvable() that  returns true if is not 0.
# ■ The methods getX() and getY() that return the solution for the equation.
# Draw the UML diagram for the class, and then implement the class. Write a test
# program that prompts the user to enter a, b, c, d, e, and f and displays the result.
# If is 0, report that “The equation has no solution.” See Exercise 4.3 for
# sample runs.

class LinearEquation:
    def __init__(self, a, b, c, d, e, f):
        self.__a = a
        self.__b = b
        self.__c = c
        self.__d = d
        self.__e = e
        self.__f = f

    #getter methods
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

    #check if equations are solvalable
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
    
a, b, c, d, e, f = eval(input("Enter values for the following a,b,c,d,e,f: "))
eq = LinearEquation(a, b, c, d, e, f)
if (eq.isSolvable()):
    print("X is:", eq.getX(), "\tY is:", eq.getY())
else:
    print("The equation is not solvable!")