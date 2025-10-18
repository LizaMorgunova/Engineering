def count_unique_elements(numbers):
    unique_numbers = set(numbers)
    sorted_unique_numbers = sorted(unique_numbers)
    return (sorted_unique_numbers, len(sorted_unique_numbers))

test1 = [1, 2, 2, 3, 4, 4, 5]
result1 = count_unique_elements(test1)
print(result1)

test2 = []
result2 = count_unique_elements(test2)
print(result2)

test3 = [-1, -2, -2, 0, 1, 0]
result3 = count_unique_elements(test3)
print(result3)

test4 = [10]
result4 = count_unique_elements(test4)
print(result4)
