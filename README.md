# CALCULADORA DE NÚMEROS COMPLEJOS
Proyecto del curso CNYT que aborda los temas fundamentales de la programación cuántica y como es el salto de lo clásico a lo cuántico, basado en sistemas y modelos físico-matemáticos.

## HERRAMIENTAS
- Lenguaje De Programación preferido, por ejemplo, PYTHON o JAVA.
- Se debe tener conocimientos de programacion ya que el proyecto debe desarrollrse Con ayuda de este.
- GITHUB: Servicio que permite alojar elementos (Para este caso un programa) versionados y realizar contribuciones y/o progresiones, en donde guardaremos nuestro proyecto.
- Libro guía: "Quantum Computing for Computer Scientists" de Noson S. Yanofsky & Mirco A. Mannucci.

# SEGUNDA ENTREGA
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
