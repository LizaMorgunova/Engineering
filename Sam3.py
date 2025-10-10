import math
one = [12, 25, 3, 48, 71]
two = [5, 18, 40, 62, 98]
three = [4, 21, 37, 56, 84]
max_values = [max(one), max(two), max(three)]
min_values = [min(one), min(two), min(three)]
def heron_area(a, b, c):
    s = (a + b + c) / 2
    return math.sqrt(s * (s - a) * (s - b) * (s - c))

area_max = heron_area(max_values[0], max_values[1], max_values[2])
area_min = heron_area(min_values[0], min_values[1], min_values[2])
print(f"Площадь треугольника с максимальными сторонами: {area_max:.2f}")
print(f"Площадь треугольника с минимальными сторонами: {area_min:.2f}")
