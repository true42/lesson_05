with open('2.txt', 'r', encoding="UTF-8") as f:
    data = f.read().split('\n')
    for i in range(len(data)):
        x = len(data[i].split())
        print(f'В строке {i+1} — {x} слов')

# import pandas as pd
# data1 = pd.read_csv('train.csv')
# print()
# print(f'Количество строк: {data1.shape[0]}\nКоличество столбцов: {data1.shape[1]}')