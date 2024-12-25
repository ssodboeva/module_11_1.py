import requests

url = "https://www.detki-psy.ru/"
response = requests.get(url)
print(response.status_code)
print(response.text)
print(response.headers['content-type'])
print(response.content)


import numpy as np

data = np.array([1, 2, 3, 4, 5])

sum_array = np.sum(data)
mean_array = np.mean(data)
squared_array = np.square(data)

print(f'Массив: {data}')
print(f'Сумма элементов: {sum_array}')
print(f'Среднее значение: {mean_array}')
print(f'Квадраты элементов: {squared_array}')



