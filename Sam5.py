def create_set_from_list(lst):
    count_dict = {}
    for number in lst:
        if number in count_dict:
            count_dict[number] += 1
        else:
            count_dict[number] = 1
    result_set = set()

    for number, count in count_dict.items():
        result_set.add(number)
        for i in range(2, count + 1):
            result_set.add(str(number) * i)
    return result_set
list_1 = [1, 1, 3, 3, 1]
list_2 = [5, 5, 5, 5, 5, 5, 5]
list_3 = [2, 2, 1, 2, 2, 5, 6, 7, 1, 3, 2, 2]

set_1 = create_set_from_list(list_1)
set_2 = create_set_from_list(list_2)
set_3 = create_set_from_list(list_3)

print(set_1)
print(set_2)
print(set_3)
