#############
## MODULOS ##
#############
from ComplexCalculator.Complx_Calculator import Cartesian
import math

########################################
## CLASE VECTOR: De numeros complejos ##
########################################
class Vector(list, object):

    def __init__(self, array):
        self.long = len(array)
        self.numbers = array.copy()

    def __str__(self, result = ""):
        if self.long == 1:
            result += "["+str(self.numbers[0])+"]"
        else:
            for i in range(self.long):
                if (0 < i < self.long-1):
                    result += str(self.numbers[i])+", "
                elif i == 0:
                    result += "["+str(self.numbers[i])+", "
                else:
                    result += str(self.numbers[i])+"]"
        return result

    def __eq__(self, other):
        if (self.long == other.long):
            for i in range(self.long):
                if not(self.numbers[i] == other.numbers[i]): return False
            return True
        else: return False

    def __add__(self, other):
        return Vector([self.numbers[i]+other.numbers[i] for i in range(self.long)])

    def __sub__(self, other):
        return Vector([self.numbers[i]-other.numbers[i] for i in range(self.long)])

    def __mul__(self, other):
        return Vector([self.numbers[i]*other.numbers[i] for i in range(self.long)])

    def conjugate(self):
        return Vector([number.conj() for number in self.numbers])

    def inverse(self):
        return Vector([number.inv() for number in self.numbers])

    def scal_prod(self, escalar):
        return Vector([escalar*number for number in self.numbers])

    def summation(self, total = Cartesian((0, 0))):
        for number in self.numbers:
            total += number
        return total

    def dot_prod(self, other):
        return (self*other).summation()

    def inner_prod(self, other):
        return (self.conjugate()*other).summation()
        
    def norm(self):
        return math.sqrt((self.inner_prod(self)).mod())

    def distance(self, other):
        return math.sqrt(((self-other).inner_prod(self-other)).mod())

#v = Vector([Cartesian((-3, -1)), Cartesian((0, -2)), Cartesian((0, 1)), Cartesian((2, 0))])
#print(v.norm())
#print(Cartesian((0, 1)).mod() )
#print(Cartesian((0, 1)).mod()/(v.norm())**2)
#print(v.conjugate())
