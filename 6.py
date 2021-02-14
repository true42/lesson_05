import re

with open('6.txt', 'r', encoding='UTF-8') as f:
    data1 = f.read().split('\n')
    print(data1)
    for i in range(len(data1)):
        result = re.sub(r'[^0-9 ]', '', data1[i])
        result = result.split()
        summa = 0
        for j in result:
            summa += int(j)
        print(f'{data1[i].split()[0]} {summa}')