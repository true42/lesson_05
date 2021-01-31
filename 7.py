import pandas as pd
import json

data = pd.read_csv('7.txt', sep=' ')
data['profit'] = pd.Series(data['income'] - data['expense'])

average_profit = {'average_profit': 0}
count = 0
firm_dict = {}

for index, row in data.iterrows():
    firm_dict[row['name']] = row['profit']
    if row['profit'] > 0:
        average_profit['average_profit'] += row['profit']
        count += 1

average_profit['average_profit'] /= count
firm_list = [firm_dict, average_profit]

with open('7.json', 'w', encoding='UTF-8') as f:
    json.dump(firm_list, f)
