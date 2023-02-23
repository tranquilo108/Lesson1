# Дан список чисел. Определите, сколько в нем
# встречается различных чисел.
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6
list1 = [1, 1, 2, 0, -1, 3, 4, 4]
list2 = [j for j in range(min(list1), max(list1) + 1)]
print(len(list2))
