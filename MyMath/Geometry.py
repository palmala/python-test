import math


class Point2D:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Point2D(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Point2D(self.x - other.x, self.y - other.y)

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def distance_to(self, another_point):
        return math.sqrt((self.x - another_point.x) ** 2 + (self.y - another_point.y) ** 2)


def is_triangle(point_a, point_b, point_c):
    if not isinstance(point_a, Point2D) or not isinstance(point_b, Point2D) or not isinstance(point_c, Point2D):
        raise AttributeError("All arguments should be Point2Ds!")
    return point_a != point_b and point_b != point_c
