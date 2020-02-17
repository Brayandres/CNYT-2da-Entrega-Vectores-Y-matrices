import math
import unittest
from Complx_Calculator import *

class Test_Complx_Calculator(unittest.TestCase):
    
    def test_add(self):
        self.assertEqual(str(Cartesian((1, 4))+Cartesian((-5, -1))), "(-4, 3)")
        #EJERCICIO: (1+4i) + (-5-i)
        self.assertEqual(str(Cartesian((12.5, math.sqrt(2)))+Cartesian((math.pi, math.sqrt(2)))),
                         "(15.641592653589793, 2.8284271247461903)")
        #EJERCICIO: (12.5+(√2)i) + (π+(√2)i)

    def test_sub(self):
        self.assertEqual(str(Cartesian((2, 10))-Cartesian((1.5, -4))), "(0.5, 14)")
        #EJERCICIO: (2+10i)-(1.5-4i)
        self.assertEqual(str(Cartesian((0, -1))-Cartesian((-1, -1))), "(1, 0)")
        #EJERCICIO: (0-i)-(-1-i)

    def test_mul(self):
        self.assertEqual(str(Cartesian((1.5, math.sqrt(2)))*Cartesian((1.5, -math.sqrt(2)))), "(4.25, 0.0)")
        #EJERCICIO: (1.5+(√2)i) * (1.5-(√2)i)
        self.assertEqual(str(Cartesian((2, -2))*Cartesian((1, 1))), "(4, 0)")
        #EJERCICIO: (2-2i) * (1+i)

    def test_div(self):
        self.assertEqual(str(Cartesian((1, -10)).div(Cartesian((10, -1)))), "("+str(20/101)+", "+str(-99/101)+")")
        #EJERCICIO: (1-10i) / (10-i)
        self.assertEqual(str(Cartesian((0, -4)).div(Cartesian((-2, 0)))), "(0.0, 2.0)")
        #EJERCICIO: (0-4i) / (-2+0i)

    def test_mod(self):
        self.assertEqual(Cartesian((2, -3)).mod(), math.sqrt(13))
        #EJERCICIO: |(2, -3)|
        self.assertEqual(Cartesian((math.sqrt(2), math.sqrt(2))).mod(), 2)
        #EJERCICIO: |(√2, √2)|

    def test_conj(self):
        self.assertEqual(str(Cartesian((1.27, -34)).conj()), "(1.27, 34)")
        #COMPLEJO: 1.27-34i
        self.assertEqual(str(Cartesian((18, 0)).conj()), "(18, 0)")
        #COMPLEJO: 18+0i

    def test_phase(self):
        self.assertEqual(phase((0, 1)), 90)
        #COMPLEJO: 0+i
        self.assertEqual(phase((-11, -1)), 185.19442890773482)
        #COMPLEJO: -11-i

    def test_cart_to_pol(self):
        self.assertEqual(str(Cartesian((-4, 2)).cart_to_pol()), "(4.47213595499958, 153.43494882292202)")
        #COMPLEJO: -4+2i
        self.assertEqual(str(Cartesian((-1, -1000000)).cart_to_pol()), "(1000000.0000005, 269.9999427042205)")
        #COMPLEJO: -1-1000000i
        
if __name__ == "__main__":
    unittest.main()
