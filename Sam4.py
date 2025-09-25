def calculate_average(*args):
    if not args:
        return 0
    total = sum(args)
    count = len(args)
    average = total / count
    return average
if __name__ == "__main__":
    result = calculate_average(10, 20, 30, 40, 50)
    print(f"Среднее арифметическое: {result}")
