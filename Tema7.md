# Тема 7. Работа с файлами (ввод, вывод)
Отчет по теме №7 подготовил(а):
- Моргунова Елизавета Денисовна
- ПИЭ-23-1

| Задание | Лаб_раб | Сам_раб |
| ------ | ------ | ------ |
| Задание 1 | + | + |
| Задание 2 | + | + |
| Задание 3 | + | + |
| Задание 4 | + | + |
| Задание 5 | + | + |
| Задание 6 | + |
| Задание 7 | + |
| Задание 8 | + |
| Задание 9 | + |
| Задание 10 | + |

знак «+» — задание выполнено; знак «–» — задание не выполнено;

## Лабораторная работа №1
### Составьте текстовый файл и положите его в одну директорию с программой на Python. Текстовый файл должен состоять минимум из двух строк.

```python
Текст в текстовом файле:
Всем привет!
Это я!
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/lab_1.jpg)

## Выводы
Создан текстовый документ с 2 сторками в одной директории с программой на Python.

## Лабораторная работа №2
### Напишите программу, которая выведет только первую строку из вашего файла, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/lab_2.jpg)

## Выводы
Код читает файл и выводит только первую строку из текстового файла.

## Лабораторная работа №3
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию open()/close().

```python
f = open('input.txt', 'r')
print(f.readline())
f.close()
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/lab_3.jpg)

## Выводы
Код читает файл и выводит строку из текстового файла.

## Лабораторная работа №4
### Напишите программу, которая выведет все строки из вашего файла в массиве, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    print(f.readlines())
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/lab_4.jpg)

## Выводы
Метод readlines() считывает все строки из файла и возвращает их в виде списка.

## Лабораторная работа №5
### Напишите программу, которая выведет каждую строку из вашего файла отдельно, при этом используйте конструкцию with open().

```python
with open('input.txt') as f:
    for line in f:
        print(line)
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/lab_5.jpg)

## Выводы
При использовании with open('input.txt') as f: и for line in f: каждая строка файла будет выводиться с символом новой строки.

## Лабораторная работа №6
### Напишите программу, которая будет добавлять новую строку в ваш файл, а потом выведет полученный файл в консоль. Вывод можно осуществлять любым способом. Обязательно проверьте сам файл, чтобы изменения в нем тоже отображались.

```python
with open('input.txt', 'a+') as f:
    f.write('\nIm additional line')
with open('input.txt', 'r') as f:
    result = f.readlines()
    print(result)
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/lab_6.jpg)

## Выводы
Код открывает файл input.txt, добавляет строку "Im additional line", затем читает и выводит все строки из файла.

## Лабораторная работа №7
### Напишите программу, которая перепишет всю информацию, которая была у вас в файле до этого, например напишет любые данные из произвольно вами составленного списка. Также не забудьте проверить что измененная вами информация сохранилась в файле.

```python
lines = ['one', 'two', 'three']
with open('input.txt', 'w') as f:
    for line in lines:
        f.write('\nCycle run ' + line)
    print('Done!')
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/lab_7_1.jpg)
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/lab_7_2.jpg)

## Выводы
В данном коде создаётся файл input.txt, в который записываются строки из списка lines. Каждая строка начинается с текста "Cycle run" и добавляется к новой строке. После завершения записи в файл выводится сообщение "Done!".

## Лабораторная работа №8
### Выберите любую папку на своем компьютере, имеющую вложенные директории. Выведите на печать в терминал ее содержимое, как и всех подкаталогов при помощи функции print_docs(directory).

```python
import os
def print_docs(directory):
    all_files = os.walk(directory)
    for catalog in all_files:
        print(f'Папка {catalog[0]} содержит:')
    print(f'Директории: {", ".join([folder for folder in catalog[1]])}')
    print(f'Файлы: {", ".join([file for file in catalog[2]])}')
    print('-' * 40)
print_docs('C:/Users/RobotComp.ru/Desktop/images/small')
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/lab_8.jpg)

## Выводы
Код предназначен для обхода указанной директории и вывода информации о папках и файлах в ней.

## Лабораторная работа №9
### Документ «input.txt» содержит следующий текст: 
### Приветствие 
### Спасибо 
### Извините 
### Пожалуйста 
### До свидания 
### Ты готов? 
### Как дела? 
### С днем рождения! 
### Удача! 
### Я тебя люблю. 
### Требуется реализовать функцию, которая выводит слово, имеющее максимальную длину (или список слов, если таковых несколько). Проверьте работоспособность программы на своем наборе данных.

```python
def longest_words(file):
    with open(file, encoding='utf-8') as f:
        words = f.read().split()
        max_length = len(max(words, key=len))
        for word in words:
            if len(word) == max_length:
                sought_words = word
        if len(sought_words) == 1:
            return sought_words[0]
        return sought_words
print(longest_words('input.txt'))
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/lab_9.jpg)

## Выводы
Функция открывает файл и считывает все слова.
Определяет максимальную длину слова.
Находит все слова, соответствующие этой длине.
Если найдено одно самое длинное слово, возвращает его; если несколько — возвращает их все.

## Лабораторная работа №10
### Требуется создать csv-файл «rows_300.csv» со следующими столбцами: 
### • № - номер по порядку (от 1 до 300);
### • Секунда – текущая секунда на вашем ПК; 
### • Микросекунда – текущая миллисекунда на часах. Для наглядности на каждой итерации цикла искусственно приостанавливайте скрипт на 0,01 секунды.

```python
import csv
import datetime
import time
with open('rows_300.csv', 'w', encoding='utf-8', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['№', 'Секунда ', 'Микросекунда'])
    for line in range(1, 301):
        writer.writerow([line, datetime.datetime.now().second,
                         datetime.datetime.now().microsecond])
    time.sleep(0.01)
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/lab_10_1.jpg)
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/lab_10_2.jpg)

## Выводы
Код создает CSV-файл, содержащий 300 строк с номером строки и значениями текущих секунд и микросекунд на момент записи. Однако из-за задержки в 0.01 секунды значения секунд могут не изменяться для каждой строки, что может привести к повторяющимся значениям в столбце "Секунда".

## Самостоятельная работа №1
### Найдите в интернете любую статью (объем статьи не менее 200 слов), скопируйте ее содержимое в файл и напишите программу, которая считает количество слов в текстовом файле и определит самое часто встречающееся слово. Результатом выполнения задачи будет: скриншот файла со статьей, листинг кода, и вывод в консоль, в котором будет указана вся необходимая информация.

```python
import re
from collections import Counter
def analyze_text_file(filepath="input.txt"):
    with open(filepath, 'r', encoding='utf-8') as file:
        text = file.read()
    text = text.lower()
    words = re.findall(r'\b\w+\b', text)
    if not words:
        print("Файл пуст или не содержит слов.")
        return 0, None, 0
    total_word_count = len(words)
    word_counts = Counter(words)
    most_common_word, most_common_count = word_counts.most_common(1)[0]
    return total_word_count, most_common_word, most_common_count
if __name__ == "__main__":
    filepath = "input.txt"
    word_count, most_frequent_word, frequency = analyze_text_file(filepath)
    if word_count > 0:
        print(f"Общее количество слов: {word_count}")
        print(f"Самое часто встречающееся слово: '{most_frequent_word}' (встречается {frequency} раз)")
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/Sam_1_1.jpg)
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/Sam_1_2.jpg)

## Выводы
Программа открывает текстовый файл и считывает его содержимое.
Обработка текста:
– Приводит текст к нижнему регистру.
– Использует регулярные выражения для извлечения слов.
Подсчет слов: Считает общее количество слов и определяет самое частое слово с помощью Counter.
Вывод результатов: Печатает общее количество слов и самое часто встречающееся слово с его частотой.

## Самостоятельная работа №2
### У вас появилась потребность в ведении книги расходов, посмотрев все существующие варианты вы пришли к выводу что вас ничего не устраивает и нужно все делать самому. Напишите программу для учета расходов. Программа должна позволять вводить информацию о расходах, сохранять ее в файл и выводить существующие данные в консоль. Ввод информации происходит через консоль. Результатом выполнения задачи будет: скриншот файла с учетом расходов, листинг кода, и вывод в консоль, с демонстрацией работоспособности программы.

```python
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
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/Sam_2_1.jpg)
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/Sam_2_2.jpg)

## Выводы
Загрузка расходов: Читает данные из файла.
Сохранение расхода: Добавляет новый расход в файл.
Добавление расхода: Запрашивает у пользователя дату, описание и сумму.
Отображение расходов: Выводит все сохраненные расходы.
Меню: Позволяет добавлять расходы, просматривать их или выходить из программы.

## Самостоятельная работа №3
### Имеется файл input.txt с текстом на латинице. Напишите программу, которая выводит следующую статистику по тексту: количество букв латинского алфавита; число слов; число строк. 
### • Текст в файле: Beautiful is better than ugly. Explicit is better than implicit. Simple is better than complex. Complex is better than complicated. 
### • Ожидаемый результат: Input file contains: 108 letters 20 words 4 lines

```python
def count_statistics(filename):
    total_letters = 0
    total_words = 0
    total_lines = 0
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            total_lines += 1
            total_letters += sum(c.isalpha() for c in line)
            total_words += len(line.split())
    return total_letters, total_words, total_lines
def main():
    filename = 'input.txt'
    letters, words, lines = count_statistics(filename)
    print(f"Input file contains: {letters} letters {words} words {lines} lines")
if __name__ == "__main__":
    main()
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/Sam_3.jpg)

## Выводы
Эта программа предназначена для анализа текстового файла, подсчитывая количество букв, слов и строк в нем. Она может быть полезна для различных задач, связанных с обработкой текста, например, для оценки длины документа или анализа его структуры.

## Самостоятельная работа №4
### Напишите программу, которая получает на вход предложение, выводит его в терминал, заменяя все запрещенные слова звездочками * (количество звездочек равно количеству букв в слове). Запрещенные слова, разделенные символом пробела, хранятся в текстовом файле input.txt. Все слова в этом файле записаны в нижнем регистре. Программа должна заменить запрещенные слова, где бы они ни встречались, даже в середине другого слова. Замена производится независимо от регистра: если файл input.txt содержит запрещенное слово exam, то слова exam, Exam, ExaM, EXAM и exAm должны быть заменены на ****. 
### • Запрещенные слова: hello email python the exam wor is 
### • Предложение для проверки: Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!! 
### • Ожидаемый результат: *****, ***ld! ****** ** *** programming language of *** future. My ***** **.... ****** ** awesome!!!!

```python
import re
def load_banned_words(filename):
    with open(filename, 'r') as file:
        return set(file.read().strip().split())
def replace_banned_words(sentence, banned_words):
    pattern = re.compile(r'\b(' + '|'.join(re.escape(word) for word in banned_words) + r')\b', re.IGNORECASE)
    def replace(match):
        return '*' * len(match.group(0))
    return pattern.sub(replace, sentence)
def main():
    banned_words = load_banned_words('input.txt')
    sentence = "Hello, world! Python IS the programming language of thE future. My EMAIL is.... PYTHON is awesome!!!!"
    print("Исходное предложение:")
    print(sentence)
    result = replace_banned_words(sentence, banned_words)
    print("\nРезультат:")
    print(result)
if __name__ == "__main__":
    main()
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/Sam_4.jpg)

## Выводы
Функция load_banned_words читает слова из файла input.txt и сохраняет их в множество.
Функция replace_banned_words ищет запрещенные слова в предложении и заменяет их на звездочки.
Основная программа:
– Загружает запрещенные слова.
– Определяет пример предложения.
– Выводит исходное предложение и результат с замененными словами.

## Самостоятельная работа №5
### Самостоятельно придумайте и решите задачу, которая будет взаимодействовать с текстовым файлом.

### Напишите программу, которая запрашивает у пользователя два числа и выводит их сумму, а потом записывает их в файл.

```python
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
```
### Результат.
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/Sam_5_1.jpg)
![Меню](https://github.com/LizaMorgunova/Software_Engineering/blob/Тема_7/pic/Sam_5_2.jpg)

## Выводы
Функция load_banned_words: Загружает запрещенные слова из файла (не используется в основном коде).
Основная функция:
– Запрашивает два числа у пользователя.
– Вычисляет их сумму и выводит результат.
– Записывает сумму в файл input.txt.

## Общие выводы по теме
Программы содержат функции, каждая из которых выполняет разные задачи, связанные с обработкой текста и числами.
1. Сложение чисел
2. Замена запрещенных слов
3. Статистика по тексту
4. Анализ текста
Они позволяет пользователю вводить числа, обрабатывать текст для замены запрещенных слов, подсчитывать статистику и анализировать текстовый файл.
