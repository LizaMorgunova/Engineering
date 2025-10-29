class Triangle:
    def __init__(self, base, height, side_a, side_b, side_c, color):
        self.__base = base
        self.__height = height
        self.__side_a = side_a
        self.__side_b = side_b
        self.__side_c = side_c
        self.__color = color
    def area(self):
        return 0.5 * self.__base * self.__height
    def perimeter(self):
        return self.__side_a + self.__side_b + self.__side_c
    def get_color(self):
        return self.__color
class EquilateralTriangle(Triangle):
    def __init__(self, side_length, color):
        super().__init__(base=side_length, height=(side_length * (3 ** 0.5)) / 2,
                         side_a=side_length, side_b=side_length, side_c=side_length,
                         color=color)
    def describe(self):
        return f"Equilateral Triangle with color {self.get_color()}: Area: {self.area()}, Perimeter: {self.perimeter()}"
equilateral_triangle = EquilateralTriangle(side_length=5, color='blue')
print(equilateral_triangle.describe())
