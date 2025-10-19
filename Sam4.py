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
