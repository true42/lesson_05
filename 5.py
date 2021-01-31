integer = [5, 6, 7, 8, 9, 10]

with open('5.txt', 'w') as f:
    for i in integer:
        f.writelines(str(i) + ' ')

with open('5.txt') as f:
    data = f.read().split()
    summa = 0
    for i in data:
        summa += int(i)
    print(summa)
