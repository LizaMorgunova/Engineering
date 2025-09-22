string = input("Введите строку: ")
length = len(string)
print("Длина строки:", length)

lower_string = string.lower()
print("Строка в нижнем регистре:", lower_string)

vowels = 'aeiouAEIOU'
vowel_count = 0
for i in string:
    if i in vowels:
        vowel_count += 1
print("Количество гласных:", vowel_count)

replaced = string.replace("ugly", "beauty")
print("Замена 'ugly' на 'beauty': ", replaced)

if string[0] == "T" and string[1] == "h" and string[2] == "e":
    print("Начинается с The")
else:
    print("Не начинается с The")
if string[len(string)-1] == "d" and string[len(string)-2] == "n" and string[len(string)-3] == "e":
    print("Заканчивается на end")
else:
    print("Не заканчивается на end")
