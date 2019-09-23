import unittest
import requests

class TestCase(unittest.TestCase):

    def test_redirect(self):
        session = requests.Session() # Инициализируем сессию
            # Объявляем переменные для работы       
        username = {'username':'user'} 
        locaton = {'city':'Moscow'}

        setCookies = 'https://httpbin.org/cookies/set'
        getCookies = 'https://httpbin.org/cookies'

        session.get(setCookies,params=username) # Отправляем get запрос для добавлени куков
        session.get(setCookies,params=locaton)  # Еще один запрос на добавление куков
        res = session.get(getCookies) # Получаем ответ о куках текущей сесии
        print(res.text) # Видим все куки добавленные ранее

if __name__ == '__main__':
    unittest.main()
