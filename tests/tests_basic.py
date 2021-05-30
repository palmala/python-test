import unittest
from MyMath import Geometry


class TestPoint2D(unittest.TestCase):
    def test_constructor(self):
        point = Geometry.Point2D()
        self.assertTrue(point.x == 0)
        self.assertTrue(point.y == 0)
        point = Geometry.Point2D(1, -1)
        self.assertTrue(point.x == 1)
        self.assertTrue(point.y == -1)

    def test_distance_to(self):
        point1 = Geometry.Point2D(0, 0)
        point2 = Geometry.Point2D(3, 4)
        self.assertTrue(point1.distance_to(point2) == 5)

    def test_addition(self):
        point1 = Geometry.Point2D(1, 2)
        point2 = Geometry.Point2D(-1, 3)
        point = point1 + point2
        self.assertTrue(point.x == 0)
        self.assertTrue(point.y == 5)

    def test_substitution(self):
        point1 = Geometry.Point2D(1, 2)
        point2 = Geometry.Point2D(1, 3)
        point = point1 - point2
        self.assertTrue(point.x == 0)
        self.assertTrue(point.y == -1)

    def test_equals(self):
        point1 = Geometry.Point2D(0, 0)
        point2 = Geometry.Point2D(1, 1)
        point3 = Geometry.Point2D(0, 1)
        self.assertFalse(point1 == point2)
        self.assertFalse(point1 == point3)


if __name__ == '__main__':
    unittest.main()
