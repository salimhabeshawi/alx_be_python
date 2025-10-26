# polymorphism_demo.py

import math

# Base Class
class Shape:
    def area(self):
        # This method is intended to be overridden by derived classes
        raise NotImplementedError("Subclasses must override the area() method.")


# Derived Class: Rectangle
class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width


# Derived Class: Circle
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)
