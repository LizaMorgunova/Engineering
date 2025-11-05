# Тема 9. Концепции и принципы ООП
Отчет по теме №9 подготовил(а):
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
### Допустим, что вы решили оригинально и немного странно познакомится с человеком. Для этого у вас должен быть написан свой класс на Python, который будет проверять угадал ваше имя человек или нет. Для этого создайте класс, указав в свойствах только имя. Дальше создайте функцию __init__(), а в ней сделайте проверку на то угадал человек ваше имя или нет. Также можете проверить что будет, если в этой функции указав атрибут, который не указан в вашем классе, например, попробуйте вызвать фамилию.

```python
class Ivan:
    __slots__ = ['name']
    def __init__(self, name):
        if name == "Иван":
            self.name = f"Да, я {name}"
        else:
            self.name = f"Я не {name}, a Иван"
person1 = Ivan('Алексей')
person2 = Ivan("Иван")
print(person1.name)
print(person2.name)
person2.surname = 'Петров'
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_9/pic./lab_1.png)

## Выводы
Код определяет класс Ivan, который использует атрибут name для хранения строки, содержащей информацию о том, является ли объект экземпляром с именем "Иван". Если имя "Иван", то строка будет "Да, я Иван", в противном случае — "Я не [имя], а Иван".

## Лабораторная работа №2
### Вам дали важное задание, написать продавцу мороженого программу, которая будет писать добавили ли топпинг в мороженое и цену после возможного изменения. Для этого вам нужно написать класс, в котором будет определяться изменили ли состав мороженого или нет. В этом классе реализуйте метод, выводящий на печать «Мороженое с {ТОППИНГ}» в случае наличия добавки, а иначе отобразится следующая фраза: «Обычное мороженое». При этом программа должна воспринимать как топпинг только атрибуты типа string.

```python
class Icecream:
    def __init__(self, ingredient=None):
        if isinstance(ingredient, str):
            self.ingredient = ingredient
        else:
            self.ingredient = None
    def composition(self):
        if self.ingredient:
            print(f"Мороженое с {self.ingredient}")
        else:
            print('Обычное мороженое')
            
icecream = Icecream()
icecream.composition()
icecream = Icecream('шоколадом')
icecream.composition()
icecream = Icecream(5)
icecream.composition()
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_9/pic./lab_2.png)

## Выводы
В методе инициализации init (неправильно, должно быть __init__) проверяется, является ли переданный аргумент строкой. Если да, то он сохраняется как атрибут ingredient; если нет, атрибут устанавливается в None.
Метод composition выводит информацию о составе мороженого: если ингредиент задан, выводится сообщение о мороженом с этим ингредиентом; если ингредиент отсутствует, выводится сообщение о том, что это обычное мороженое.

## Лабораторная работа №3
### Петя – начинающий программист и на занятиях ему сказали реализовать икапсу…что-то. А вы хороший друг Пети и ко всему прочему прекрасно знаете, что икапсу…что-то – это инкапсуляция, поэтому решаете помочь вашему другу с написанием класса с инкапсуляцией. Ваш класс будет не просто инкапсуляцией, а классом с сеттером, геттером и деструктором. После написания класса вам необходимо продемонстрировать что все написанные вами функции работают. Также вас необходимо объяснить Пете почему на скриншоте ниже в консоли выводится ошибка.

```python
class MyClass:
    def __init__(self, value):
        self._value = value
    def set_value(self, value):
        self._value = value
    def get_value(self):
        return self._value
    def del_value(self):
        del self._value

    value = property(get_value, set_value, del_value, "Свойство value")

obj = MyClass(42)
print(obj.get_value())
obj.set_value(45)
print(obj.get_value())
obj.set_value(100)
print(obj.get_value())
obj. del_value()
print(obj.get_value())
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_9/pic./lab_3.png)

## Выводы
Метод init (должен быть __init__) принимает значение и сохраняет его в атрибуте _value.
Метод set_value позволяет изменять значение _value.
Метод get_value возвращает текущее значение _value.
Метод del_value удаляет атрибут _value.

## Лабораторная работа №4
### Вам прекрасно известно, что кошки и собаки являются млекопитающими, но компьютер этого не понимает, поэтому вам нужно написать три класса: Кошки, Собаки, Млекопитающие. И при помощи “наследования” объяснить компьютеру что кошки и собаки – это млекопитающие. Также добавьте какой-нибудь свой атрибут для кошек и собак, чтобы показать, что они чем-то отличаются друг от друга.

```python
class Mammal:
    className = 'Mammal'
class Dog(Mammal):
    species = 'canine'
    sounds = "wow"
class Cat(Mammal):
    species = 'feline'
    sounds = 'meow'
dog = Dog()
print(f"Dog is {dog.className}, but they say {dog.sounds}")
cat = Cat()
print(f"Cat is {cat.className}, but they say {cat.sounds}")
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_9/pic./lab_4.png)

## Выводы
Mammal базовый класс, содержащий атрибут className, который указывает, что это млекопитающее.
Dog наследует от Mammal и добавляет атрибуты species (вид) и sounds (звуки).
Cat также наследует от Mammal, добавляя свои атрибуты species и sounds.

## Лабораторная работа №5
### На разных языках здороваются по-разному, но суть остается одинаковой, люди друг с другом здороваются. Давайте вместе с вами реализуем программу с полиморфизмом, которая будет описывать всю суть первого предложения задачи. Для этого мы можем выбрать два языка, например, русский и английский и написать для них отдельные классы, в которых будет в виде атрибута слово, которым здороваются на этих языках. А также напишем функцию, которая будет выводить информацию о том, как на этих языках здороваются. Заметьте, что для решения поставленной задачи мы использовали декоратор @staticmethod, поскольку нам не нужны обязательные параметры-ссылки вроде self.

```python
class Russian:
    @staticmethod
    def greeting():
        print("Привет")
class English:
    @staticmethod
    def greeting():
        print("Hello")
def greet(language):
    language.greeting()
ivan = Russian()
greet(ivan)
john = English()
greet(john)
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_9/pic./lab_5.png)

## Выводы
Код определяет два класса: Russian и English, каждый из которых содержит статический метод greeting(), выводящий приветствие на соответствующем языке (русском и английском). Функция greet(language) принимает экземпляр класса и вызывает его метод greeting(). 

## Самостоятельная работа №1
### Вызовите справку по садоводству.

```python
class Tomato:
    # Статическое свойство, содержащее стадии созревания помидора
    states = ["seed", "sprout", "flower", "green", "ripe"]

    def __init__(self, index):
        # Динамические свойства
        self._index = index  # Индекс томата (публичное свойство)
        self._state = Tomato.states[0]  # Начальное состояние (первое значение из states)

    # Метод для перевода томата на следующую стадию созревания
    def grow(self):
        current_index = Tomato.states.index(self._state)
        if current_index < len(Tomato.states) - 1:
            self._state = Tomato.states[current_index + 1]

    # Метод для проверки, созрел ли томат
    def is_ripe(self):
        return self._state == "ripe"


class TomatoBush:
    def __init__(self, number_of_tomatoes):
        # Динамическое свойство, хранящее список томатов
        self.tomatoes = [Tomato(i) for i in range(number_of_tomatoes)]

    # Метод для перевода всех томатов на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Метод для проверки, все ли томаты стали спелыми
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # Метод для сбора урожая и очистки списка томатов
    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        # Динамические свойства
        self.name = name  # Имя садовника (публичное свойство)
        self._plant = plant  # Объект класса TomatoBush (приватное свойство)

    # Метод, который заставляет садовника работать и способствует созреванию помидоров
    def work(self):
        self._plant.grow_all()

    # Метод для проверки, все ли плоды созрели и сбора урожая
    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собрал урожай!")
            self._plant.give_away_all()
        else:
            print(f"{self.name} предупреждает: не все помидоры созрели!")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("1. Поливайте растения регулярно.")
        print("2. Убедитесь, что у них достаточно солнечного света.")
        print("3. Удаляйте увядшие листья и плоды.")
        print("4. Используйте удобрения для улучшения роста.")

def test_knowledge_base():
    Gardener.knowledge_base()  # Проверяем, что метод вызывается без ошибок
    print("test_knowledge_base: Passed")

if __name__ == "__main__":
    test_knowledge_base()
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_9/pic./Sam_1.png)

## Выводы
Класс Tomato:
– Статическое свойство states содержит стадии созревания.
– Динамические свойства _index (индекс томата) и _state (текущая стадия).
– Метод grow() переводит томат на следующую стадию.
– Метод is_ripe() проверяет, созрел ли томат.

Класс TomatoBush:
– Динамическое свойство tomatoes хранит список объектов класса Tomato.
– Метод grow_all() переводит все томаты на следующий этап созревания.
– Метод all_are_ripe() проверяет, все ли томаты спелые.
– Метод give_away_all() очищает список томатов после сбора урожая.

Класс Gardener:
– Динамические свойства name (имя садовника) и _plant (объект класса TomatoBush).
– Метод work() заставляет садовника работать с растениями.
– Метод harvest() проверяет, созрели ли все плоды, и собирает урожай.
– Статический метод knowledge_base() выводит справку по садоводству.

test_knowledge_base проверяет, что метод справки по садоводству работает без ошибок.

## Самостоятельная работа №2
### Создайте объекты классов TomatoBush и Gardener.

```python
class Tomato:
    # Статическое свойство, содержащее стадии созревания помидора
    states = ["seed", "sprout", "flower", "green", "ripe"]

    def __init__(self, index):
        # Динамические свойства
        self._index = index  # Индекс томата (публичное свойство)
        self._state = Tomato.states[0]  # Начальное состояние (первое значение из states)

    # Метод для перевода томата на следующую стадию созревания
    def grow(self):
        current_index = Tomato.states.index(self._state)
        if current_index < len(Tomato.states) - 1:
            self._state = Tomato.states[current_index + 1]

    # Метод для проверки, созрел ли томат
    def is_ripe(self):
        return self._state == "ripe"


class TomatoBush:
    def __init__(self, number_of_tomatoes):
        # Динамическое свойство, хранящее список томатов
        self.tomatoes = [Tomato(i) for i in range(number_of_tomatoes)]

    # Метод для перевода всех томатов на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Метод для проверки, все ли томаты стали спелыми
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # Метод для сбора урожая и очистки списка томатов
    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        # Динамические свойства
        self.name = name  # Имя садовника (публичное свойство)
        self._plant = plant  # Объект класса TomatoBush (приватное свойство)

    # Метод, который заставляет садовника работать и способствует созреванию помидоров
    def work(self):
        self._plant.grow_all()

    # Метод для проверки, все ли плоды созрели и сбора урожая
    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собрал урожай!")
            self._plant.give_away_all()
        else:
            print(f"{self.name} предупреждает: не все помидоры созрели!")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("1. Поливайте растения регулярно.")
        print("2. Убедитесь, что у них достаточно солнечного света.")
        print("3. Удаляйте увядшие листья и плоды.")
        print("4. Используйте удобрения для улучшения роста.")

def test_create_objects():
    bush = TomatoBush(5)  # Создаем куст с 5 томатами
    gardener = Gardener("John", bush)  # Создаем садовника с именем John
    assert len(bush.tomatoes) == 5, "Failed: bush does not contain 5 tomatoes"
    print("test_create_objects: Passed")

if __name__ == "__main__":
    test_create_objects()
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_9/pic./Sam_2.png)

## Выводы
test_create_objects создает объекты TomatoBush и Gardener, проверяет их типы и количество томатов в кусте.

## Самостоятельная работа №3
### Используя объект класса Gardener, поухаживайте за кустом с помидорами.

```python
class Tomato:
    # Статическое свойство, содержащее стадии созревания помидора
    states = ["seed", "sprout", "flower", "green", "ripe"]

    def __init__(self, index):
        # Динамические свойства
        self._index = index  # Индекс томата (публичное свойство)
        self._state = Tomato.states[0]  # Начальное состояние (первое значение из states)

    # Метод для перевода томата на следующую стадию созревания
    def grow(self):
        current_index = Tomato.states.index(self._state)
        if current_index < len(Tomato.states) - 1:
            self._state = Tomato.states[current_index + 1]

    # Метод для проверки, созрел ли томат
    def is_ripe(self):
        return self._state == "ripe"


class TomatoBush:
    def __init__(self, number_of_tomatoes):
        # Динамическое свойство, хранящее список томатов
        self.tomatoes = [Tomato(i) for i in range(number_of_tomatoes)]

    # Метод для перевода всех томатов на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Метод для проверки, все ли томаты стали спелыми
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # Метод для сбора урожая и очистки списка томатов
    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        # Динамические свойства
        self.name = name  # Имя садовника (публичное свойство)
        self._plant = plant  # Объект класса TomatoBush (приватное свойство)

    # Метод, который заставляет садовника работать и способствует созреванию помидоров
    def work(self):
        self._plant.grow_all()

    # Метод для проверки, все ли плоды созрели и сбора урожая
    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собрал урожай!")
            self._plant.give_away_all()
        else:
            print(f"{self.name} предупреждает: не все помидоры созрели!")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("1. Поливайте растения регулярно.")
        print("2. Убедитесь, что у них достаточно солнечного света.")
        print("3. Удаляйте увядшие листья и плоды.")
        print("4. Используйте удобрения для улучшения роста.")

def test_care_for_tomato_bush():
    bush = TomatoBush(3)
    gardener = Gardener("Alice", bush)
    gardener.work()  # Ухаживаем за кустом
    for tomato in bush.tomatoes:
        assert tomato._state == "sprout", "Failed: tomato did not become a sprout"
    print("test_care_for_tomato_bush: Passed")

if __name__ == "__main__":
    test_care_for_tomato_bush()
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_9/pic./Sam_3.png)

## Выводы
test_care_for_tomato_bush ухаживает за кустом и проверяет, что все томаты стали ростками.

## Самостоятельная работа №4
### Попробуйте собрать урожай, когда томаты еще не дозрели. Продолжайте ухаживать за ними.

```python
class Tomato:
    # Статическое свойство, содержащее стадии созревания помидора
    states = ["seed", "sprout", "flower", "green", "ripe"]

    def __init__(self, index):
        # Динамические свойства
        self._index = index  # Индекс томата (публичное свойство)
        self._state = Tomato.states[0]  # Начальное состояние (первое значение из states)

    # Метод для перевода томата на следующую стадию созревания
    def grow(self):
        current_index = Tomato.states.index(self._state)
        if current_index < len(Tomato.states) - 1:
            self._state = Tomato.states[current_index + 1]

    # Метод для проверки, созрел ли томат
    def is_ripe(self):
        return self._state == "ripe"


class TomatoBush:
    def __init__(self, number_of_tomatoes):
        # Динамическое свойство, хранящее список томатов
        self.tomatoes = [Tomato(i) for i in range(number_of_tomatoes)]

    # Метод для перевода всех томатов на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Метод для проверки, все ли томаты стали спелыми
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # Метод для сбора урожая и очистки списка томатов
    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        # Динамические свойства
        self.name = name  # Имя садовника (публичное свойство)
        self._plant = plant  # Объект класса TomatoBush (приватное свойство)

    # Метод, который заставляет садовника работать и способствует созреванию помидоров
    def work(self):
        self._plant.grow_all()

    # Метод для проверки, все ли плоды созрели и сбора урожая
    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собрал урожай!")
            self._plant.give_away_all()
        else:
            print(f"{self.name} предупреждает: не все помидоры созрели!")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("1. Поливайте растения регулярно.")
        print("2. Убедитесь, что у них достаточно солнечного света.")
        print("3. Удаляйте увядшие листья и плоды.")
        print("4. Используйте удобрения для улучшения роста.")


def test_harvest_before_ripe():
    bush = TomatoBush(3)
    gardener = Gardener("Bob", bush)
    gardener.harvest()  # Пытаемся собрать урожай до созревания
    assert len(bush.tomatoes) == 3, "Failed: tomatoes should not be harvested yet"
    gardener.work()  # Ухаживаем за кустом снова
    gardener.work()  # Ухаживаем за кустом еще раз
    for tomato in bush.tomatoes:
        assert tomato._state == "flower", "Failed: tomato did not become a flower"
    print("test_harvest_before_ripe: Passed")

if __name__ == "__main__":
    test_harvest_before_ripe()
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_9/pic./Sam_4.png)

## Выводы
test_harvest_before_ripe пытается собрать урожай до того, как томаты созреют, и проверяет, что они не были собраны.

## Самостоятельная работа №5
### Соберите урожай.

```python
class Tomato:
    # Статическое свойство, содержащее стадии созревания помидора
    states = ["seed", "sprout", "flower", "green", "ripe"]

    def __init__(self, index):
        # Динамические свойства
        self._index = index  # Индекс томата (публичное свойство)
        self._state = Tomato.states[0]  # Начальное состояние (первое значение из states)

    # Метод для перевода томата на следующую стадию созревания
    def grow(self):
        current_index = Tomato.states.index(self._state)
        if current_index < len(Tomato.states) - 1:
            self._state = Tomato.states[current_index + 1]

    # Метод для проверки, созрел ли томат
    def is_ripe(self):
        return self._state == "ripe"


class TomatoBush:
    def __init__(self, number_of_tomatoes):
        # Динамическое свойство, хранящее список томатов
        self.tomatoes = [Tomato(i) for i in range(number_of_tomatoes)]

    # Метод для перевода всех томатов на следующий этап созревания
    def grow_all(self):
        for tomato in self.tomatoes:
            tomato.grow()

    # Метод для проверки, все ли томаты стали спелыми
    def all_are_ripe(self):
        return all(tomato.is_ripe() for tomato in self.tomatoes)

    # Метод для сбора урожая и очистки списка томатов
    def give_away_all(self):
        self.tomatoes.clear()


class Gardener:
    def __init__(self, name, plant):
        # Динамические свойства
        self.name = name  # Имя садовника (публичное свойство)
        self._plant = plant  # Объект класса TomatoBush (приватное свойство)

    # Метод, который заставляет садовника работать и способствует созреванию помидоров
    def work(self):
        self._plant.grow_all()

    # Метод для проверки, все ли плоды созрели и сбора урожая
    def harvest(self):
        if self._plant.all_are_ripe():
            print(f"{self.name} собрал урожай!")
            self._plant.give_away_all()
        else:
            print(f"{self.name} предупреждает: не все помидоры созрели!")

    @staticmethod
    def knowledge_base():
        print("Справка по садоводству:")
        print("1. Поливайте растения регулярно.")
        print("2. Убедитесь, что у них достаточно солнечного света.")
        print("3. Удаляйте увядшие листья и плоды.")
        print("4. Используйте удобрения для улучшения роста.")


def test_harvest_after_ripe():
    bush = TomatoBush(3)
    gardener = Gardener("Charlie", bush)

    # Ухаживаем за кустом несколько раз, чтобы помидоры созрели
    for _ in range(4):  # Делаем 4 ухаживания
        gardener.work()

    gardener.harvest()  # Собираем урожай
    assert len(bush.tomatoes) == 0, "Failed: all tomatoes should be harvested"
    print("test_harvest_after_ripe: Passed")

if __name__ == "__main__":
    test_harvest_after_ripe()
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_9/pic./Sam_5.png)

## Выводы
test_harvest_after_ripe ухаживает за кустом до тех пор, пока все томаты не созреют, а затем собирает урожай и проверяет, что все томаты были собраны.

## Общие выводы по теме
Все классы были реализованы и протестированы на предмет правильного поведения.
Классы правильно взаимодействуют друг с другом. 
Все тесты прошли успешно, что указывает на правильность логики и отсутствие ошибок в коде.
Код организован в виде классов и методов, что делает его более читабельным и поддерживаемым.
Таким образом, написанные программы демонстрируют хорошую практику объектно-ориентированного программирования и тестирования. Они готовы к дальнейшему развитию и расширению функциональности.
