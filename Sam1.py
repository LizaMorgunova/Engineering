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
