def load_expenses(filename):
    with open(filename, 'r', encoding='utf-8') as file:
        return [line.strip() for line in file.readlines()]
def save_expense(expense, filename):
    with open(filename, 'a', encoding='utf-8') as file:
        file.write(expense + '\n')
def add_expense():
    date = input("Введите дату (ГГГГ-ММ-ДД): ")
    description = input("Введите описание расхода: ")
    amount = input("Введите сумму расхода: ")
    expense = f"{date} | {description} | {amount}"
    save_expense(expense, 'text.txt')
    print("Расход успешно добавлен!")
def display_expenses(expenses):
    if not expenses:
        print("Нет записанных расходов.")
        return
    print("\nВаши расходы:")
    for expense in expenses:
        print(expense)
def main():
    filename = "text.txt"
    expenses = load_expenses(filename)
    while True:
        print("\nМеню:")
        print("1. Добавить расход")
        print("2. Показать все расходы")
        print("3. Выход")
        choice = input("Выберите действие (1/2/3): ")
        if choice == '1':
            add_expense()
        elif choice == '2':
            display_expenses(expenses)
            expenses = load_expenses(filename)
        elif choice == '3':
            print("Выход из программы.")
            break
        else:
            print("Неверный выбор. Пожалуйста, попробуйте снова.")
if __name__ == "__main__":
    main()
