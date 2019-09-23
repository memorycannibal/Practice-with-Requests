import unittest
import requests

class TestCase(unittest.TestCase):

    def test_get(self):
        #Пример работы с json ответом
        res = requests.get('https://api.github.com/events')
        res = res.json()
        print(res[0]["actor"]["login"])    

        #Отправка json через post
        json = {"testjson":"testvalue"}
        res = requests.post("http://httpbin.org/post",json=json)
        print(res.text)




if __name__ == '__main__':
    unittest.main()
