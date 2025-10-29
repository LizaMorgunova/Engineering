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
