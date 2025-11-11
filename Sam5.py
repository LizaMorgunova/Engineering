# Определяем собственное исключение
class NegativeNumberError(Exception):
    """Исключение, которое возникает при вводе отрицательного числа."""
    pass

def check_positive_number(num):
    """Проверяет, является ли число положительным."""
    if num < 0:
        raise NegativeNumberError(f"Ошибка: {num} - это отрицательное число!")
    return num

def calculate_square(num):
    """Возвращает квадрат положительного числа."""
    try:
        check_positive_number(num)
        return num ** 2
    except NegativeNumberError as e:
        print(e)

def main():
    """Основная функция, которая запрашивает у пользователя ввод числа и вычисляет его квадрат."""
    for _ in range(2):  # Запрашиваем два числа
        try:
            user_input = float(input("Введите положительное число: "))
            square = calculate_square(user_input)
            if square is not None:
                print(f"Квадрат числа {user_input} равен {square}.")
        except ValueError:
            print("Ошибка: Введите корректное число.")

if __name__ == "__main__":
    main()
