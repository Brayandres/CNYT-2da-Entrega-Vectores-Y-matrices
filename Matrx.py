#########################
## MODULOS Y LIBRERIAS ##
#########################
from ComplexCalculator.Complx_Calculator import Cartesian
from Vector import Vector
import math

########################################
## CLASE MATRX: De Vectores Complejos ##
########################################
class Matrx(Vector, object):
    def __init__(self, array):
        self.longRow = len(array)
        self.longColumn = array[0].long
        self.rows = array.copy()
        self.columns = []
        for j in range(self.longColumn):
            temp =[]
            for i in range(len(array)):
                temp.append(array[i].numbers[j])
            (self.columns).append(Vector(temp))

    def __str__(self):
        result = ""
        for i in range(self.longRow):
            if i < self.longRow-1:
                result += str(self.rows[i])+"\n"
            else:
                result += str(self.rows[i])
        return result
    
    def __eq__(self, other):
        if (self.longRow == other.longRow) and (self.longColumn == other.longColumn):
            for i in range(self.longRow):
                if not(self.rows[i] == other.rows[i]):
                    return False
            return True
        else: return False

    def __add__(self, other):
        return Matrx([self.rows[i]+other.rows[i] for i in range(self.longRow)])

    def __sub__(self, other):
        return Matrx([self.rows[i]-other.rows[i] for i in range(self.longRow)])

    def __mul__(self, other):
        result = []
        for i in range(self.longRow):
            vectTemp = []
            for j in range(other.longColumn):
                vectTemp.append(self.rows[i].dot_prod(other.columns[j]))
            result.append(Vector(vectTemp))
        return Matrx(result)

    def conjugate(self):
        return Matrx([row.conjugate() for row in self.rows])

    def addInverse(self):
        return Matrx([row.inverse() for row in self.rows])

    def scalarProd(self, scalar):
        return Matrx([row.scal_prod(scalar) for row in self.rows])

    def transposed(self):
        temp = []
        for j in range(self.longColumn):
            temp.append(self.columns[j])
        self = Matrx(temp)
        return self

    def dagger(self):
        return (self.transposed()).conjugate()

    def tensorProduct(self, other):
        result = []; vectTemp = []
        for k in range(self.longRow):
            for i in range(other.longRow):
                vectTemp = []
                for j in range(self.longColumn):
                    vectTemp += (other.rows[i].scal_prod(self.rows[k].numbers[j])).numbers
                result.append(Vector(vectTemp))
        return Matrx(result)

    def actOnVect(self, vector):
        return (self*Matrx([vector]).transposed()).columns[0]

    def identity(self):
        result =[]
        for i in range(self.longRow):
            temp = []
            for j in range(self.longRow):
                if i == j:temp.append(Cartesian((1, 0)))
                else: temp.append(Cartesian((0, 0)))
            result.append(Vector(temp))
        return Matrx(result)

    def delta(self, value):
        return (self-(self.identity()).scalarProd(value))

    def isHermitian(self):
        if self == self.dagger():
            return True
        return False

    def isUnitary(self):
        if (self*self.dagger() == self.dagger()*self == self.identity()):
            return True
        return False
