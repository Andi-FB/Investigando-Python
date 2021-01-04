"""
The aim of this exercise is to create a new numeric style class.
You should create a new user defined class called Distance. It will be very
similar to Quantity.
You should be able to add two distances together, subtract one distance from
another, divide a distance by an integer, multiply a distance by an integer etc.
"""


class Distance:

    def __init__(self, quantity):
        self.quantity = quantity

    def __add__(self, other):
        quantity = self.quantity + other.quantity
        return Distance(quantity)

    def __sub__(self, other):
        quantity = self.quantity - other.quantity
        return Distance(quantity)

    def __mul__(self, other):
        if isinstance(other, Distance):
            quantity = self.quantity * other.quantity
        else:
            quantity = self.quantity * other
        return Distance(quantity)

    def __floordiv__(self, other):
        if isinstance(other, Distance):
            quantity = self.quantity // other.quantity
        else:
            quantity = self.quantity // other
        return Distance(quantity)

    def __truediv__(self, other):
        if isinstance(other, Distance):
            quantity = self.quantity / other.quantity
        else:
            quantity = self.quantity / other
        return Distance(quantity)

    def __str__(self):
        return 'Distance({})'.format(self.quantity)


d1 = Distance(6)
d2 = Distance(3)
print(d1 + d2)
print(d1 - d2)
print(d1 / 2)
print(d1 / d2)
print(d2 // 2)
print(d2 // d1)
print(d2 * 2)
print(d2 * d1)
