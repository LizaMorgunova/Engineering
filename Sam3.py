n = int(input())
if n > 0 and n < 11:
    if n > 0 and n < 4:
        print("Число от 0 до 3")
    if n > 3 and n < 6:
        print("Число от 3 до 6")
    if n > 5 and n < 11:
        print("Число от 6 до 10")
else:
    print("Неправильное число")
