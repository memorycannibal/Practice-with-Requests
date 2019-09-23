import unittest
import requests

class TestCase(unittest.TestCase):

    def test_get(self):
        res = requests.get('https://swapi.co/api/people/1')
        print("Статус ответа: {}".format( res.status_code) )
        print("Время ожидания ответа: {}".format( res.elapsed.total_seconds() ))

        print("Хидеры: {}".format( res.headers ))
        print("Текст ответа: ")
        print(res.text)




if __name__ == '__main__':
    unittest.main()