a = set('abcdefg')
print(a)
for i in range(1, 5):
    a.add(i)
print(a)


a = frozenset('abcdefg')
print(a)
for i in range(1, 5):
    a.add(i)
print(a)
