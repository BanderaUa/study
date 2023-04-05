import requests


class test_new_joke():
    """Создание новой шутки"""

    def __init__(self):
        pass

    # def test_create_new_random_joke(self):
    #     url = "https://api.chucknorris.io/jokes/random"
    #     print(url)
    #     result = requests.get(url)
    #     print("Статус код: " + str(result.status_code))
    #     assert 200 == result.status_code
    #     if result.status_code == 200:
    #         print("Выполнено успешно!")
    #     else:
    #         print("Ошибка! Проверьте правильность данных!")
    #     check = result.json()
    #     # check_info= check.get("categories")
    #     # print(check_info)
    #     # assert check_info == []
    #     # print("Категория верна")
    #     check_info_value = check.get("value")
    #     print(check_info_value)
    #     name = "Chuck"
    #     if name in check_info_value:
    #         print("chuck присутсвует")
    #     else:
    #         print("Отсутствует")


    def test_create_new_random_joke_categories(self):
        """создание шутки по категории"""
        category = 'sport'
        url = "https://api.chucknorris.io/jokes/random?category=" + category
        print(url)
        result = requests.get(url)
        print("Статус код: " + str(result.status_code))
        assert 200 == result.status_code
        if result.status_code == 200:
            print("Выполнено успешно!")
        else:
            print("Ошибка! Проверьте правильность данных!")
        check = result.json()
        check_info= check.get("categories")
        print(check_info)
        assert check_info == ['sport']
        print("Категория верна")
        # check_info_value = check.get("value")
        # print(check_info_value)
        # name = "Chuck"
        # if name in check_info_value:
        #     print("chuck присутсвует")
        # else:
        #     print("Отсутствует")


# joking = test_new_joke()
# joking.test_create_new_random_joke()

var_1 = test_new_joke()
var_1.test_create_new_random_joke_categories()






