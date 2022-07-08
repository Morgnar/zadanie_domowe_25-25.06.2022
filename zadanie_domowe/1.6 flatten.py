"""
1.6 flatten
Napisz funkcję spłaszczającą zagnieżdzone listy:
assert flatten([[1, 2], [3, 4]]) == [1, 2, 3, 4]
assert flatten([[1, 2], [3, 4, [5, 6]]]) == [1, 2, 3, 4, 5, 6]

"""

list1 = [[1, 2], [3, 4]]
list2 = []

print(list1[0])
x = len(list1)

for i in range(0, x - 1):
    list2 += list1[i]

print(list2)


??????