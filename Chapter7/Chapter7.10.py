# 7.10 (The Time class) Design a class named Time. The class contains:
# ■ The private data fields hour, minute, and second that represent a time.
# ■ A constructor that constructs a Time object that initializes hour, minute, and
# second using the current time.
# ■ The get methods for the data fields hour, minute, and second, respectively.
# ■ A method named setTime(elapseTime) that sets a new time for the object
# using the elapsed time in seconds. For example, if the elapsed time is 555550
# seconds, the hour is 10, the minute is 19, and the second is 12.
# Draw the UML diagram for the class, and then implement the class. Write a test
# program that creates a Time object and displays its hour, minute, and second.
# Your program then prompts the user to enter an elapsed time, sets its elapsed
# time in the Time object, and displays its hour, minute, and second.
import time

class Time:
    def __init__(self):
        self.setTime(int(time.time()))
    
    # getter methods
    def getHour(self):
        return self.__hour
    
    def getMinute(self):
        return self.__minute

    def getSecond(self):
        return self.__second

    # setTime
    def setTime(self,elapseTime):
        self.__second = elapseTime%60
        totalMinutes = elapseTime//60
        self.__minute = totalMinutes%60
        totalHours = totalMinutes//60
        self.__hour = totalHours%24

currTime = Time()
elapsedTime= eval(input("Enter the time elapsed"))
currTime.setTime(elapsedTime)
print("The elapse time is HR:MIN:SEC",currTime.getHour(), ":", currTime.getMinute(), ":", currTime.getSecond())
