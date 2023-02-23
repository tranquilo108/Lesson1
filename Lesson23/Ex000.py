a = int(input('Введите количество рассматриваемых дней: '))
b = list(input('Введите температуру для каждого дня: ').split(' '))
temp = 0
max_ = 0


for i in range(a):
    if int(b[i]) > 0:
        temp += 1
    else:
        temp = 0
    if temp > max_:
        max_ = temp


print(max_)
