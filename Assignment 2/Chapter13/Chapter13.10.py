# 13.10 (The Rational class) Modify the Rational class in Listing 8.4, Rational.py, to
# throw a RuntimeError exception if the d is 0.

class Rational:
    def __init__(self, n=0, d=1):
        if d == 0:
            raise RuntimeError()

        divisor = gcd(n, d)
        self.__n = (1 if d > 0 else -1) \
                           * int(n / divisor)
        self.__d = int(abs(d) / divisor)

    def __add__(self, Rational_2):
        n = self.__n * Rational_2[1] + \
            self.__d * Rational_2[0]
        d = self.__d * Rational_2[1]
        return Rational(n, d)

    def __sub__(self, Rational_2):
        n = self.__n * Rational_2[1] - \
            self.__d * Rational_2[0]
        d = self.__d * Rational_2[1]
        return Rational(n, d)

    def __mul__(self, Rational_2):
        n = self.__n * Rational_2[0]
        d = self.__d * Rational_2[1]
        return Rational(n, d)

    def __truediv__(self, Rational_2):
        n = self.__n * Rational_2[1]
        d = self.__d * Rational_2[0]
        return Rational(n, d)

    def __float__(self):
        return self.__n / self.__d

    def __int__(self):
        return int(self.__float__())

    def __str__(self):
        if self.__d == 1:
            return str(self.__n)
        else:
            return str(self.__n) + "/" + str(self.__d)

    def __lt__(self, Rational_2):
        return self.__cmp__(Rational_2) < 0

    def __le__(self, Rational_2):
        return self.__cmp__(Rational_2) <= 0

    def __gt__(self, Rational_2):
        return self.__cmp__(Rational_2) > 0

    def __ge__(self, Rational_2):
        return self.__cmp__(Rational_2) >= 0

    # Compare two numbers
    def __cmp__(self, Rational_2):
        temp = self.__sub__(Rational_2)
        if temp[0] > 0:
            return 1
        elif temp[0] < 0:
            return -1
        else:
            return 0

    def __getitem__(self, index):
        if index == 0:
            return self.__n
        else:
            return self.__d

def gcd(n, d):
    n1 = abs(n)
    n2 = abs(d)
    gcd = 1
    k = 1
    while k <= n1 and k <= n2:
        if n1 % k == 0 and n2 % k == 0:
            gcd = k
        k += 1
    return gcd

def main():
    try:
        n1 = Rational(5, 10)
        n2 = Rational(1, 0)
        print(n1 + n2)
    except RuntimeError:
        print("Exp: Cannot divide by Zero!")
main()