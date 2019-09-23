import unittest
import requests

class TestCase(unittest.TestCase):

    def test_header(self):
        header = {"Content-Type":"multipart/form-data"}
        res = requests.get('http://httpbin.org/post',headers=header)
        print("Content-Type запроса: {}".format(res.request.headers["Content-Type"])) #Видим успешное применение нашего Content-Type
        print("Content-Type ответа: {}".format(res.headers["Content-Type"]))#Видим Content-Type, полученый от сервера



if __name__ == '__main__':
    unittest.main()