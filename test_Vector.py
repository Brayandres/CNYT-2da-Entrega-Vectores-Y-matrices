import unittest
from Vector import *
#Vector([Cartesian((, )), Cartesian((, )), Cartesian((, ))])

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








