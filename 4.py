data1 = []
with open('4.txt', 'r', encoding="UTF-8") as f:
    data = f.read().split('\n')
    for i in range(len(data)):
        if data[i][-1] == '1':
            data1.append('Один ' + data[i][-3:] + '\n')
        elif data[i][-1] == '2':
            data1.append('Два ' + data[i][-3:] + '\n')
        elif data[i][-1] == '3':
            data1.append('Три ' + data[i][-3:] + '\n')
        elif data[i][-1] == '4':
            data1.append('Четыре ' + data[i][-3:])

with open('4_.txt', 'w', encoding='UTF-8') as f:
    f.writelines(data1)
