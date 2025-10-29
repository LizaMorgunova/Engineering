import math
class Shape:
    def area(self):
        raise NotImplementedError("Subclasses must implement this method")
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def area(self):
        return self.width * self.height
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return math.pi * (self.radius ** 2)
def print_area(shape):
    print(f"The area of the shape is: {shape.area()}")
shapes = [
    Triangle(base=5, height=10),
    Rectangle(width=4, height=6),
    Circle(radius=3)
]
for shape in shapes:
    print_area(shape)
