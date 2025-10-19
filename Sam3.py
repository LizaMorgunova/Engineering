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
