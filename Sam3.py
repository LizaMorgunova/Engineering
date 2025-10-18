def count_digits(sequence):
    digit_count = {}
    for char in sequence:
        if char.isdigit():
            digit = int(char)
            if digit in digit_count:
                digit_count[digit] += 1
            else:
                digit_count[digit] = 1
    sorted_digits = sorted(digit_count.items(), key=lambda item: item[1], reverse=True)[:3]
    top_three = {key: value for key, value in sorted(sorted_digits)}
    return top_three
sequence = "12345678901234567890"
result = count_digits(sequence)
print(result) 
