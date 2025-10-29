# Тема 8. Введение в ООП
Отчет по теме №8 подготовил(а):
- Моргунова Елизавета Денисовна
- ПИЭ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |

знак «+» — задание выполнено; знак «–» — задание не выполнено;

## Лабораторная работа №1
### Создайте класс “Car” с атрибутами производитель и модель. Создайте объект этого класса. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями.

```python
# Определяем класс Car (Автомобиль)
class Car:
    # Метод инициализации (конструктор) класса Car
    def __init__(self, make, model):
        # Присваиваем атрибут make (марка) объекту
        self.make = make
        # Присваиваем атрибут model (модель) объекту
        self.model = model
# Создаем экземпляр класса Car с маркой "Toyota" и моделью "Corolla"
my_car = Car("Toyota", "Corolla")
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_8/pic/lab_1.png)

## Выводы
1. class Car: — создаёт новый класс с именем Car.
2. def init(self, make, model): — это метод, который должен инициализировать объект, но он неправильно назван. Правильное название — __init__.
3. self.make = make и self.model = model — присваивают значения параметров make и model атрибутам объекта.
4. my_car = Car("Toyota", "Corolla") — пытается создать объект my_car класса Car, но из-за ошибки в названии метода инициализации это приведёт к ошибке.

## Лабораторная работа №2
### Дополните код из первого задания, добавив в него атрибуты и методы класса, заставьте машину “поехать”. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def drive(self):
        print(f"Driving the {self.make} {self.model}")
my_car = Car("Toyota", "Corolla")
my_car.drive()
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_8/pic/lab_2.png)

## Выводы
Методы __init__ и drive устанавливают марку и модель автомобиля и выводят сообщение о движении. При создании экземпляра my_car атрибуты не инициализируются, что приводит к ошибке при вызове my_car.drive().

## Лабораторная работа №3
### Создайте новый класс “ElectricCar” с методом “charge” и атрибутом емкость батареи. Реализуйте его наследование от класса, созданного в первом задании. Заставьте машину поехать, а потом заряжаться. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль. 

```python
class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def drive(self):
        print(f"Driving the {self.make} {self.model}")
my_car = Car("Toyota", "Corolla")
my_car.drive()
class ElectricCar(Car):
    def __init__(self, make, model, battery_capacity):
        super().__init__(make, model)
        self.battery_capacity = battery_capacity
    def charge(self):
        print(f"Charging the {self.make} {self.model} with {self.battery_capacity} kWh")
my_electric_car = ElectricCar("Tesla", "Model S", 75)
my_electric_car.drive()
my_electric_car.charge()
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_8/pic/lab_3.png)

## Выводы
Car:
– Конструктор принимает make и model.
– Метод drive() выводит сообщение о движении.
ElectricCar:
– Добавляет параметр battery_capacity.
– Метод charge() сообщает о зарядке.

## Лабораторная работа №4
### Реализуйте инкапсуляцию для класса, созданного в первом задании. Создайте защищенный атрибут производителя и приватный атрибут модели. Вызовите защищенный атрибут и заставьте машину поехать. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
class Car:
    def __init__(self, make, model):
        self._make = make # Защищенный атрибут
        self. __model = model # Приватный атрибут
    def drive(self):
        print(f"Driving the {self._make} {self.__model}")
my_car = Car("Toyota", "Corolla")
print(my_car._make)
my_car.drive()
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_8/pic/lab_4.png)

## Выводы
Конструктор init:
– Принимает два параметра: make (марка) и model (модель).
– Создаёт защищённый атрибут _make и приватный атрибут __model.
Метод drive:
– Выводит сообщение о том, что автомобиль движется, используя марку и модель.
Создание экземпляра my_car:
– Создаётся объект класса Car с маркой "Toyota" и моделью "Corolla".
Вывод значения защищённого атрибута _make:
– Печатает марку автомобиля.
Вызов метода drive:
– Выводит сообщение о движении автомобиля.

## Лабораторная работа №5
### Реализуйте полиморфизм создав основной (общий) класс “Shape”, а также еще два класса “Rectangle” и “Circle”. Внутри последних двух классов реализуйте методы для подсчета площади фигуры. После этого создайте массив с фигурами, поместите туда круг и прямоугольник, затем при помощи цикла выведите их площади. Напишите комментарии для кода, объясняющие его работу. Результатом выполнения задания будет листинг кода с комментариями и получившийся вывод в консоль.

```python
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
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_8/pic/lab_5.png)

## Выводы
Shape содержит абстрактный метод area(), который должен быть реализован в дочерних классах.
Rectangle инициализируется с шириной и высотой, а метод area() вычисляет площадь как произведение этих значений.
Circle инициализируется с радиусом, а метод area() вычисляет площадь по формуле πr².

## Самостоятельная работа №1
### Самостоятельно создайте класс и его объект. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_8/pic/Sam_1.png)

## Выводы
Класс Triangle определяет треугольник с атрибутами для основания, высоты и сторон.
Конструктор инициализирует эти атрибуты при создании объекта.
Метод area вычисляет площадь треугольника по формуле  ½ × основание × высота .
Метод perimeter суммирует длины всех сторон для вычисления периметра.
Создание объекта создает треугольник с заданными параметрами.
Вычисление площади и периметра, затем вывод результатов.

## Самостоятельная работа №2
### Самостоятельно создайте атрибуты и методы для ранее созданного класса. Они должны отличаться, от тех, что указаны в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_8/pic/Sam_2.png)

## Выводы
Атрибуты:
– base, height: основание и высота треугольника.
– side_a, side_b, side_c: длины трех сторон.
– color: цвет треугольника.
Методы:
– area(): вычисляет площадь треугольника.
– perimeter(): вычисляет периметр треугольника.
– is_equilateral(): проверяет, равны ли все три стороны (равносторонний треугольник).
– is_isosceles(): проверяет, есть ли две равные стороны (равнобедренный треугольник).
– describe(): возвращает описание треугольника, включая его тип и цвет.
В конце создается объект треугольника с заданными параметрами, и выводятся его площадь, периметр и описание. 

## Самостоятельная работа №3
### Самостоятельно реализуйте наследование, продолжая работать с ранее созданным классом. Оно должно отличаться, от того, что указано в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_8/pic/Sam_3.png)

## Выводы
Triangle - базовый класс для треугольников с методами для вычисления площади и периметра.
EquilateralTriangle наследует Triangle, принимает длину стороны и цвет, вычисляет высоту.
Создается равносторонний треугольник с длиной стороны 5 и цветом 'blue', выводится его описание.

## Самостоятельная работа №4
### Самостоятельно реализуйте инкапсуляцию, продолжая работать с ранее созданным классом. Она должна отличаться, от того, что указана в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_8/pic/Sam_4.png)

## Выводы
1. Все атрибуты класса Triangle начинаются с двойного подчеркивания (__), что делает их приватными.
2. Мы сохранили методы для вычисления площади и периметра.
3. Добавлен один простой геттер для получения цвета треугольника.
4. В классе EquilateralTriangle мы используем конструктор родительского класса для инициализации.

## Самостоятельная работа №5
### Самостоятельно реализуйте полиморфизм. Он должен отличаться, от того, что указан в теоретическом материале (методичке) и лабораторных заданиях. Результатом выполнения задания будет листинг кода и получившийся вывод консоли.

```python
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
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_8/pic/Sam_5.png)

## Выводы
1. Базовый класс Shape - это абстрактный класс с методом area(), который должен быть реализован в подклассах.
2. Подклассы:
– Triangle реализует метод area() для вычисления площади треугольника.
– Rectangle реализует метод area() для вычисления площади прямоугольника.
– Circle реализует метод area() для вычисления площади круга.
3. Функция print_area принимает объект типа Shape и вызывает его метод area(), демонстрируя полиморфизм.

## Общие выводы по теме
Наследование позволяет создавать иерархии классов, избегая дублирования кода.
Разные классы могут иметь методы с одинаковыми именами, но с разной реализацией.
Разделение кода на классы и методы облегчает тестирование и повторное использование.
Хорошо структурированный код с понятными именами легче читать и поддерживать.
Абстрактные классы определяют общий интерфейс для подклассов, упрощая работу с различными типами объектов.
Методы для расчета площади и периметра демонстрируют применение математических формул в коде.
Легко добавлять новые фигуры, расширяя функциональность программы.
Применение стандартных библиотек, таких как math, для выполнения общих задач.
