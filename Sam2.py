class Triangle:
    def __init__(self, base, height, side_a, side_b, side_c, color):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
        self.color = color
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
    def is_equilateral(self):
        return self.side_a == self.side_b == self.side_c
    def is_isosceles(self):
        return (self.side_a == self.side_b) or (self.side_a == self.side_c) or (self.side_b == self.side_c)
    def describe(self):
        triangle_type = "Equilateral" if self.is_equilateral() else "Isosceles" if self.is_isosceles() else "Scalene"
        return f"This is a {triangle_type} triangle with color {self.color}."
triangle = Triangle(base=10, height=8, side_a=10, side_b=10, side_c=6, color="blue")
area = triangle.area()
perimeter = triangle.perimeter()
description = triangle.describe()
print(f"Area: {area}")
print(f"Perimeter: {perimeter}")
print(description)
