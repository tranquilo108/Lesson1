F = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610]
A = int(input('Введите одно из чисел последовательности: '))


if A in F:
    print(F.index(A) + 1)
elif A == 1:
    print('2 or 3')
else:
    print(-1)


# def fibonacci(n):
#     if n in (1, 2):
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
 
 
# print(fibonacci(10))