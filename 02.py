# Дан список, вывести отдельно буквы и цифры, пользуясь filter.

data = [12, 'sadfewg', 423, 15354, "ttttdsdffg"]
print(data)
res = list(filter(lambda x: type(x) == int , data))
res2 = list(filter(lambda x: type(x) == str , data))
print(f'Числа: {res}')
print(f'Строки: {res2}')