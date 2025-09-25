import math
def calculate_area(a, b, c):
    s = (a + b + c) / 2
    area = math.sqrt(s * (s - a) * (s - b) * (s - c))
    return area


from lab import calculate_area
def main():
    print("Вычисление площади треугольника по формуле Герона.")
    a = float(input("Введите длину стороны a: "))
    b = float(input("Введите длину стороны b: "))
    c = float(input("Введите длину стороны c: "))
    area = calculate_area(a, b, c)
    print(f"Площадь треугольника: {area:}")
if __name__ == "__main__":
    main()
