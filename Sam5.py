def load_banned_words(filename):
    with open(filename, 'r') as file:
        return set(file.read().strip().split())
def main():
    num1 = float(input("Введите первое число: "))
    num2 = float(input("Введите второе число: "))
    total = num1 + num2
    print(f"Сумма {num1} и {num2} равна {total}")
    with open("input.txt", "a") as file:
        file.write(f"{total}\n")
if __name__ == "__main__":
    main()
