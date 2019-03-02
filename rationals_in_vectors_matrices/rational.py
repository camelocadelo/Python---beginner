from numbers import *


def gcd(a, b):
    if a == 0 and b == 0:
        raise ArithmeticError("gcd(0,0) does not exist")
    while b:
        a, b = b, a % b
    return a


class Rational( Number ) :
    def __init__( self, num, denum = 1 ) :
        self. num = num
        self. denum = denum
        self. normalize( )

    def normalize(self):
        if self.denum != 0:
            div = gcd(self.num, self.denum)
            if div != 1 or div != -1:
                self.num = self.num // div
                self.denum = self.denum // div
            if self.denum < 0:
                self.num *= -1
                self.denum *= -1

    def __repr__( self ) :
        if self.denum != 1:
            return "{}/{}".format(self.num, self.denum)
        else:
            return "{}".format(self.num)

    def __neg__(self):
        return Rational(-self.num, self.denum)

    def __add__ ( self, other ) :
        if not isinstance ( other, Rational ) :
            return Rational( other*self.denum + self.num, self.denum )
        else:
            return Rational( self.num * other.denum + other.num * self. denum, 
                           self.denum * other. denum )

    def __sub__ ( self, other ) :
        if not isinstance ( other, Rational ) :
            return Rational( self.num - other * self.denum, self.denum )
        else:
            return Rational( self.num * other.denum - other.num * self.denum, 
                           self.denum * other.denum )

    def __radd__ ( self, other ) :
         return self.__add__( other )

    def __rsub__ ( self, other ) :
         return self.__sub__( other )

    def __mul__( self, other ) :
         if not isinstance( other, Rational ) :
             return Rational( self.num * other, self.denum )
         else:
             return Rational( self.num * other.num, self.denum * other.denum )

    def __truediv__( self, other ) :
         if not isinstance ( other, Rational ) :
             return Rational( self.num, self.denum * other )
         else:
             return Rational( self.num * other.denum, self.denum * other.num )

    def __rmul__ ( self, other ) :
         return self.__mul__( other )

    def __rtruediv__( self, other ) :
         return self.__truediv__( other )
