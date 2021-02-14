x = '0'
with open("1.txt", "a", encoding="UTF-8") as f:
    while x != '':
        x = input("Введите данные: ")
        f.writelines(f'{x}\n')
