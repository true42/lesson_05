import pandas as pd

data = pd.read_csv('3.txt', header=None)

for index, row in data.iterrows():
    if row[1] < 20000:
        print(row[0])

print(f'Средняя зарплата: {data[1].sum()/data.shape[0]}')
