# Задача №23.
# Дан массив, состоящий из целых чисел. Напишите
# программу, которая подсчитает количество
# элементов массива, больших предыдущего (элемента
# с предыдущим номером)
# Input: [0, -1, 5, 2, 3]
# Output: 2 (-1 < 5, 2 < 3)
list1 = [0, -1, 2, 5, 2, 3, 4]
temp = -100000000000000000000
count = -1
for i in list1:
    if temp < i:
        count += 1
    temp = i
print(count)

