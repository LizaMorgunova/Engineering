checks = [
    8734, 2345, 8201, 6621, 9999, 1234, 5678, 8201, 8888, 4321,
    3365, 1478, 9865, 5555, 7777, 9998, 1111, 2222, 3333, 4444,
    5556, 6666, 5410, 7778, 8889, 4445, 1439, 9604, 8201, 3365,
    7502, 3016, 4928, 5837, 8201, 2643, 5017, 9682, 8530, 3250,
    7193, 9051, 4506, 1987, 3365, 5410, 7168, 7777, 9865, 5678,
    8201, 4445, 3016, 4506, 4506
]
total_checks = len(checks)
unique_visitors = len(set(checks))

visitor_counts = {}
for check in checks:
    if check in visitor_counts:
        visitor_counts[check] += 1
    else:
        visitor_counts[check] = 1

most_frequent_visitor = None
max_visits = -1

for visitor, count in visitor_counts.items():
    if count > max_visits:
        max_visits = count
        most_frequent_visitor = visitor

# Вывод результатов в консоль
print(f"Выдано чеков {total_checks}")
print(f"Посетило ресторан {unique_visitors}")
print(f"Работник {most_frequent_visitor} посетил ресторан больше всех раз")
