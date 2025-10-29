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
    def describe(self):
        return f"Triangle with color {self.color}: Area: {self.area()}, Perimeter: {self.perimeter()}"
class EquilateralTriangle(Triangle):
    def __init__(self, side_length, color):
        super().__init__(base=side_length, height=(side_length * (3 ** 0.5)) / 2,
                         side_a=side_length, side_b=side_length, side_c=side_length,
                         color=color)
    def describe(self):
        return f"Equilateral Triangle with color {self.color}: Area: {self.area()}, Perimeter: {self.perimeter()}"
equilateral_triangle = EquilateralTriangle(side_length=5, color='blue')
print(equilateral_triangle.describe())
