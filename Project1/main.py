class Rectangle:
    def __init__(self, lowleft, upright):
        self.lowleft = lowleft
        self.upright = upright


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def falls_in_rectangle(self, rectangle):
        if (rectangle.lowleft[0] < self.x < rectangle.upright[0]
                and rectangle.lowleft[1] < self.y < rectangle.upright[1]):
            return True
        else:
            return False


point1 = Point(6, 7)
rectangle1 = Rectangle((5, 6), (10, 12))

print(point1.falls_in_rectangle(rectangle1))