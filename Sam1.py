import time

# Декоратор для измерения времени выполнения функции
def time_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()  # Запоминаем время начала
        result = func(*args, **kwargs)  # Вызываем оригинальную функцию
        end_time = time.time()  # Запоминаем время окончания
        execution_time = end_time - start_time  # Вычисляем время выполнения
        print(f"Время выполнения функции '{func.__name__}': {execution_time:.6f} секунд")
        return result
    return wrapper

@time_decorator
def fibonacci():
    fib1 = fib2 = 1
    for i in range(2, 200):
        fib1, fib2 = fib2, fib1 + fib2
    print(fib2, end='')

if __name__ == "__main__":
    fibonacci()
