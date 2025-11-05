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
