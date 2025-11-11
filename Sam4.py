import time
from functools import wraps

# Определяем декоратор
def timing_decorator(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Запоминаем время начала выполнения
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию
        end_time = time.time()  # Запоминаем время окончания выполнения
        execution_time = end_time - start_time  # Вычисляем время выполнения
        print(f"Функция '{func.__name__}' выполнена за {execution_time:.4f} секунд.")
        return result
    return wrapper

# Применяем декоратор к первой функции
@timing_decorator
def calculate_sum(n):
    """Функция для вычисления суммы чисел от 1 до n."""
    return sum(range(1, n + 1))

# Применяем декоратор ко второй функции
@timing_decorator
def factorial(n):
    """Функция для вычисления факториала числа n."""
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)

# Тестирование функций
if __name__ == "__main__":
    print("Сумма чисел от 1 до 100:", calculate_sum(100))
    print("Факториал числа 5:", factorial(5))
