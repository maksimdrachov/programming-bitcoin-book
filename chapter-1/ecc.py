class FieldElement:

    def __init__(self, num, prime):
        if num >= prime or num<0:
            error = 'Num {} not in field range 0 to {}'.format(num, prime-1)
            raise ValueError(error)
        self.num = num
        self.prime = prime
    
    def __repr__(self):
        return 'FieldElement_{}({})'.format(self.prime, self.num)

    def __eq__(self, other):
        if other is None:
            return False
        return self.num == other.num and self.prime == other.prime
    
    def __ne__(self, other):
        equal = self.__eq__(other)
        return (not equal)

    def __add__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cannot add two numbers in different fields")
        num = (self.num + other.num)%self.prime
        return self.__class__(num, self.prime)
    
    def __sub__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cannot subtract two numbers in different fields")
        num = (self.num - other.num)%self.prime
        return self.__class__(num, self.prime)

    def __mul__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cannot multiply two numbers in different fields")
        num = (self.num * other.num)%self.prime
        return self.__class__(num, self.prime)

    def __pow__(self, exponent):
        #num = (self.num ** exponent) % self.prime
        #num = pow(self.num, exponent, self.prime)
        n = exponent % (self.prime - 1)
        num = pow(self.num, n, self.prime)
        return self.__class__(num, self.prime)
    
    def __truediv__(self, other):
        if self.prime != other.prime:
            raise TypeError("Cannot divide two numbers in different fields")
        result = self.__mul__(other.__pow__(self.prime-2))
        return self.__class__(result.num, result.prime)