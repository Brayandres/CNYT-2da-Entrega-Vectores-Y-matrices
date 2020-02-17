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
