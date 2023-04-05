import requests
url = "https://api.chucknorris.io/jokes/random"
print(url)
result = requests.get(url)
print(result)
print("Статус код: " + str(result.status_code))
assert 200 == result.status_code
if result.status_code == 200:
    print("Выполнено успешно!")
else:
    print("Ошибка! Проверьте правильность данных!")
