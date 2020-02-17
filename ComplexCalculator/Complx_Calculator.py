import math

class Complx(object):

    def __init__(self, tupl):
        self.element_1 = roundingNumb(tupl[0])
        self.element_2 = roundingNumb(tupl[1])

    def __str__(self):
        return "(" + str(self.element_1) + ", " + str(self.element_2) + ")"

    def __eq__(self, other):
        if (self.element_1 == other.element_1) and (self.element_2 == other.element_2): return True
        return False

class Cartesian(Complx):
    def __init__(self, tupl):
        super().__init__(tupl)
        self.real = self.element_1
        self.imag = self.element_2

    def __add__(self, other):
        return Cartesian((self.real + other.real, self.imag + other.imag))
    
    def __sub__(self, other):
        return Cartesian((self.real - other.real, self.imag - other.imag))

    def __mul__(self, other):
        return Cartesian((self.real*other.real-self.imag*other.imag, self.real*other.imag+self.imag*other.real))

    def div(self, other):
        return Cartesian( ((self.real*other.real + self.imag*other.imag)/((other.real**2)+(other.imag**2)),
                           (self.imag*other.real - self.real*other.imag)/((other.real**2)+(other.imag**2))) )

    def conj(self):
        return Cartesian((self.real, -self.imag))

    def inv(self):
        return Cartesian((-self.real, -self.imag))

    def cart_to_pol(self):
        return Pol(( (Cartesian((self.element_1, self.element_2))).mod(), phase((self.element_1, self.element_2)) ))

    def mod(self):
        return roundingNumb(math.sqrt((self.real**2) + (self.imag**2)))

class Pol(Complx):    
    def __init__(self, tupl):
        super().__init__(tupl)
        self.ratio = self.element_1
        self.theta = self.element_2*(math.pi/180)

    def pol_to_cart(self):
        return Cartesian((self.ratio*math.cos(self.theta), self.ratio*math.sin(self.theta)))

def phase(tupl):
    #Casos particulares, angulos rectos
    if tupl[0] == tupl[1] == 0: return 0
    elif tupl[0] == 0 and tupl[1] > 0: return 90
    elif tupl[0] == 0 and tupl[1] < 0: return 270
    elif tupl[1] == 0 and tupl[0] > 0: return 0
    elif tupl[1] == 0 and tupl[0] < 0: return 180
    #Caso general, primer cuadrante
    elif (tupl[0] > 0) and (tupl[1] > 0):
        return math.atan(tupl[1]/tupl[0])*(180/math.pi)
    #Caso general, segundo y tercer cuadrante
    elif (tupl[0] < 0):
        return math.atan(tupl[1]/tupl[0])*(180/math.pi) + 180
    #Caso general, cuarto cuadrante
    elif (tupl[0] > 0) and (tupl[1] < 0):
        return math.atan(tupl[1]/tupl[0])*(180/math.pi) + 360

def roundingNumb(a):
    n = abs(a)
    if   (round(n, 10) - math.floor(n)) == 0: return round(a)
    elif (math.ceil(n) - round(n, 10)) == 0: return round(a)
    else: return a
