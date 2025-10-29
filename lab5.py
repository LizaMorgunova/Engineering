class Shape:
    # Базовый класс для всех фигур
    def area(self):
        # Абстрактный метод для вычисления площади
        pass
class Rectangle(Shape):
    # Класс для прямоугольника, наследующий от Shape
    def __init__(self, width, height):
        # Конструктор, инициализирующий ширину и высоту
        self.width = width
        self.height = height
    def area(self):
        # Метод для вычисления площади прямоугольника
        return self.width * self.height
class Circle(Shape):
    # Класс для круга, наследующий от Shape
    def __init__(self, radius):
        # Конструктор, инициализирующий радиус
        self.radius = radius
    def area(self):
        # Метод для вычисления площади круга по формуле πr²
        return 3.14 * self.radius * self.radius
