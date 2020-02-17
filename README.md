# PROYECTO COMPUTACIÓN CUÁNTICA CNYT
Proyecto del curso CNYT que aborda los temas fundamentales de la programación cuántica y como es el salto de lo clásico a lo cuántico, basado en sistemas y modelos físico-matemáticos.

## HERRAMIENTAS
- Lenguaje De Programación preferido, por ejemplo, PYTHON o JAVA.
- Se debe tener conocimientos de programacion ya que el proyecto debe desarrollrse Con ayuda de este.
- GITHUB: Servicio que permite alojar elementos (Para este caso un programa) versionados y realizar contribuciones y/o progresiones, en donde guardaremos nuestro proyecto.
- Libro guía: "Quantum Computing for Computer Scientists" de Noson S. Yanofsky & Mirco A. Mannucci.

# SEGUNDA ENTREGA (CALCULADORA VECTORES-MATRICES)
Para Esta segunda entrega se tiene una calculadora de **vectores** y **matrices** _complejas_ que permite realizar distintas operaciones entre ellos para poder operar de manera adecuada.

## REQUISITOS
La librería debe incluir las siguientes operaciones:
- 1. Adición de vectores complejos.
- 2. Inverso (aditivo) de un vector complejo.
- 3. Multiplicación de un escalar por un vector complejo.
- 4. Adición de matrices complejas.
- 5. Inversa (aditiva) de una matriz compleja.
- 6. Multiplicación de un escalar por una matriz compleja.
- 7. Transpuesta de una matriz/vector.
- 8. Conjugada de una matriz/vector.
- 9. Adjunta (daga) de una matriz/vector.
- 10. Producto de dos matrices (de tamaños compatibles).
- 11. Función para calcular la "acción" de una matriz sobre un vector.
- 12. Producto interno de dos vectores.
- 13. Norma de un vector.
- 14. Distancia entre dos vectores.
- 15. Revisar si una matriz es unitaria.
- 16. Revisar si una matriz es Hermitiana.
- 17. Producto tensor de dos matrices/vectores.

## LIBRERIA
### VECTORES
```Python
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
© 2020 GitHub, Inc.
```

### MATRICES
```Python
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
```

## PRUEBAS
### VECTORES
```Python
import unittest
from Vector import *

class Test_Vector(unittest.TestCase):

    def test_add(self):
        v1 = Vector([Cartesian((8, 3)), Cartesian((-1, -4)), Cartesian((0, -9))])
        v2 = Vector([Cartesian((8, -3)), Cartesian((2, 5)), Cartesian((3, 0))])
        self.assertEqual(str(v1+v2), "[(16, 0), (1, 1), (3, -9)]")

    def test_inverse(self):
        v = Vector([Cartesian((-5, 2)), Cartesian((3, 0)), Cartesian((0, -1))])
        self.assertEqual(str(v.inverse()), "[(5, -2), (-3, 0), (0, 1)]")

    def test_scal_prod(self):
        c = Cartesian((-1, 1))
        v = Vector([Cartesian((-2, 5)), Cartesian((-1, -1)), Cartesian((2, -9))])
        self.assertEqual(str(v.scal_prod(c)), "[(-3, -7), (2, 0), (7, 11)]")

    def test_inner_prod(self):
        v1 = Vector([Cartesian((2, -1)), Cartesian((-8, -5)), Cartesian((-2, -6))])
        v2 = Vector([Cartesian((6, -3)), Cartesian((5, -1)), Cartesian((-6, -2))])
        self.assertEqual(str(v1.inner_prod(v2)), "(4, 1)")

    def test_norm(self):
        v = Vector([Cartesian((4, 5)), Cartesian((3, 1)), Cartesian((0, -7))])
        self.assertEqual(v.norm(), 10)

    def test_distance(self):
        v1 = Vector([Cartesian((2, 7)), Cartesian((4, -1)), Cartesian((2, -4))])
        v2 = Vector([Cartesian((7, 8)), Cartesian((2, -8)), Cartesian((1, 4))])
        self.assertEqual(v1.distance(v2), 12)
        v3 = Vector([Cartesian((9, -7)), Cartesian((-1, -6))])
        v4 = Vector([Cartesian((7, -8)), Cartesian((5, -9))])
        self.assertEqual(v3.distance(v4), 7.0710678118654755)

if __name__ == "__main__":
    unittest.main()
```
### MATRICES
```Python
import unittest
from Matrx import *
import math

class Test_Matrx(unittest.TestCase):

    def test_add(self):
        m1 = Matrx([Vector([Cartesian((-8, -3)), Cartesian((-6, -4)), Cartesian((0, -4))]),
                    Vector([Cartesian((-1, 8)), Cartesian((6, -10)), Cartesian((8, -5))]),
                    Vector([Cartesian((4, 0)), Cartesian((8, 5)), Cartesian((-7, -9))])])
        m2 = Matrx([Vector([Cartesian((-7, -2)), Cartesian((-4, -2)), Cartesian((7, 7))]),
                    Vector([Cartesian((5, 9)), Cartesian((0, 3)), Cartesian((6, -5))]),
                    Vector([Cartesian((1, 5)), Cartesian((-6, -6)), Cartesian((5, 8))])])
        m3 = Matrx([Vector([Cartesian((-15, -5)), Cartesian((-10, -6)), Cartesian((7, 3))]),
                    Vector([Cartesian((4, 17)), Cartesian((6, -7)), Cartesian((14, -10))]),
                    Vector([Cartesian((5, 5)), Cartesian((2, -1)), Cartesian((-2, -1))])])

        self.assertEqual(m1 + m2, m3)

    def test_addInverse(self):
        m = Matrx([Vector([Cartesian((7, 3)), Cartesian((-1, 7))]),
                   Vector([Cartesian((-9, -4)), Cartesian((-7, -9))])])
        mAI = Matrx([Vector([Cartesian((-7, -3)), Cartesian((1, -7))]),
                     Vector([Cartesian((9, 4)), Cartesian((7, 9))])])
        
        self.assertEqual(m.addInverse(), mAI)

    def test_scalarProd(self):
        c = Cartesian((-2, 3))
        m = Matrx([Vector([Cartesian((3, -2)), Cartesian((8, -4))]),
                   Vector([Cartesian((4, -10)), Cartesian((-2, -8))])])
        cm = Matrx([Vector([Cartesian((0, 13)), Cartesian((-4, 32))]),
                    Vector([Cartesian((22, 32)), Cartesian((28, 10))])])
        
        self.assertEqual(m.scalarProd(c), cm)

    def test_transposed(self):
        m = Matrx([Vector([Cartesian((5, 9)), Cartesian((-7, -5)), Cartesian((-1, -4))]),
                   Vector([Cartesian((8, 2)), Cartesian((-3, -7)), Cartesian((7, -8))])])
        mT = Matrx([Vector([Cartesian((5, 9)), Cartesian((8, 2))]),
                    Vector([Cartesian((-7, -5)), Cartesian((-3, -7))]),
                    Vector([Cartesian((-1, -4)), Cartesian((7, -8))])])
        
        self.assertEqual(m.transposed(), mT)

    def test_conjugate(self):
        m = Matrx([Vector([Cartesian((-6, 1)), Cartesian((3, 8))]),
                   Vector([Cartesian((2, -6)), Cartesian((3, 0))])])
        mC = Matrx([Vector([Cartesian((-6, -1)), Cartesian((3, -8))]),
                    Vector([Cartesian((2, 6)), Cartesian((3, 0))])])

        self.assertEqual(m.conjugate(), mC)

    def test_dagger(self):
        m = Matrx([Vector([Cartesian((7, 7)), Cartesian((3, 8)), Cartesian((8, 4))]),
                   Vector([Cartesian((5, 0)), Cartesian((8, -6)), Cartesian((-10, -1))])])
        mD = Matrx([Vector([Cartesian((7, -7)), Cartesian((5, 0))]),
                    Vector([Cartesian((3, -8)), Cartesian((8, 6))]),
                    Vector([Cartesian((8, -4)), Cartesian((-10, 1))])])

        self.assertEqual(m.dagger(), mD)

    def test_mul(self):
        a = Matrx([Vector([Cartesian((-6, 2)), Cartesian((0, 6)), Cartesian((7, 2))]),
                   Vector([Cartesian((6, 9)), Cartesian((7, 7)), Cartesian((-6, -6))]),
                   Vector([Cartesian((5, 8)), Cartesian((-6, 8)), Cartesian((6, 9))])])
        b = Matrx([Vector([Cartesian((9, -6)), Cartesian((-3, -4)), Cartesian((5, -2))]),
                   Vector([Cartesian((3, 6)), Cartesian((-1, -5)), Cartesian((0, -5))]),
                   Vector([Cartesian((9, 9)), Cartesian((8, -4)), Cartesian((-8, -4))])])
        c = Matrx([Vector([Cartesian((-33, 153)), Cartesian((120, 0)), Cartesian((-44, -22))]),
                   Vector([Cartesian((87, 0)), Cartesian((-26, -117)), Cartesian((107, 70))]),
                   Vector([Cartesian((0, 165)), Cartesian((147, 26)), Cartesian((69, -36))])])

        self.assertEqual(a*b, c)

    def test_actOnVect(self):
        m = Matrx([Vector([Cartesian((-1, 5)), Cartesian((1, -7)), Cartesian((-6, 3))]),
                   Vector([Cartesian((-3, -9)), Cartesian((2, -5)), Cartesian((1, -10))]),
                   Vector([Cartesian((-6, 5)), Cartesian((6, -5)), Cartesian((3, -2))])])
        v = Vector([Cartesian((1, -3)), Cartesian((4, 3)), Cartesian((-3, 1))])
        mv = Vector([Cartesian((54, -32)), Cartesian((0, 17)), Cartesian((41, 30))])

        self.assertEqual(m.actOnVect(v), mv)

    def test_isUnitary(self):
        a = Matrx([Vector([Cartesian((1/math.sqrt(2), 0)), Cartesian((0, 1/math.sqrt(2)))]),
                   Vector([Cartesian((0, 1/math.sqrt(2))), Cartesian((1/math.sqrt(2), 0))])])
        b = Matrx([Vector([Cartesian((0, 1)), Cartesian((1, 0)), Cartesian((0, 0))]),
                   Vector([Cartesian((0, 0)), Cartesian((0, 1)), Cartesian((1, 0))]),
                   Vector([Cartesian((1, 0)), Cartesian((0, 0)), Cartesian((0, 1))])])

        self.assertEqual(a.isUnitary(), True)
        self.assertEqual(b.isUnitary(), False)

    def test_isHermitian(self):
        a = Matrx([Vector([Cartesian((3, 0)), Cartesian((2, -1)), Cartesian((0, -3))]),
                   Vector([Cartesian((2, 1)), Cartesian((0, 0)), Cartesian((1, -1))]),
                   Vector([Cartesian((0, 3)), Cartesian((1, 1)), Cartesian((0, 0))])])
        b = Matrx([Vector([Cartesian((1, 0)), Cartesian((3, -1))]),
                   Vector([Cartesian((3, 1)), Cartesian((0, 1))])])
        
        self.assertEqual(a.isHermitian(), True)
        self.assertEqual(b.isHermitian(), False)

    def test_tensorProduct(self):
        a = Matrx([Vector([Cartesian((1, 1)), Cartesian((0, 0))]),
                   Vector([Cartesian((1, 0)), Cartesian((0, 1))])])
        b = Matrx([Vector([Cartesian((-1, 2)), Cartesian((-2, -2)), Cartesian((0, 2))]),
                   Vector([Cartesian((2, 3)), Cartesian((3, 1)), Cartesian((2, 2))]),
                   Vector([Cartesian((-2, 1)), Cartesian((1, -1)), Cartesian((2, 1))])])
        c = Matrx([Vector([Cartesian((-3, 1)), Cartesian((0, -4)), Cartesian((-2, 2)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0))]),
                   Vector([Cartesian((-1, 5)), Cartesian((2, 4)), Cartesian((0, 4)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0))]),
                   Vector([Cartesian((-3, -1)), Cartesian((2, 0)), Cartesian((1, 3)), Cartesian((0, 0)), Cartesian((0, 0)), Cartesian((0, 0))]),
                   Vector([Cartesian((-1, 2)), Cartesian((-2, -2)), Cartesian((0, 2)), Cartesian((-2, -1)), Cartesian((2, -2)), Cartesian((-2, 0))]),
                   Vector([Cartesian((2, 3)), Cartesian((3, 1)), Cartesian((2, 2)), Cartesian((-3, 2)), Cartesian((-1, 3)), Cartesian((-2, 2))]),
                   Vector([Cartesian((-2, 1)), Cartesian((1, -1)), Cartesian((2, 1)), Cartesian((-1, -2)), Cartesian((1, 1)), Cartesian((-1, 2))])])

        self.assertEqual(a.tensorProduct(b), c)

if __name__ == "__main__":
    unittest.main()
```
