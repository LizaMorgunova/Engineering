class Triangle:
    def __init__(self, base, height, side_a, side_b, side_c):
        self.base = base
        self.height = height
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c
    def area(self):
        return 0.5 * self.base * self.height
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
triangle = Triangle(base=10, height=5, side_a=7, side_b=8, side_c=9)
triangle_area = triangle.area()
triangle_perimeter = triangle.perimeter()
print(f"Площадь треугольника: {triangle_area}")
print(f"Периметр треугольника: {triangle_perimeter}")
