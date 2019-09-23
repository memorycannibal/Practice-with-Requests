import unittest
import requests

class TestCase(unittest.TestCase):

    def test_redirect(self):
        res = requests.get('http://github.com')
        print(res.status_code) # Видим успешный переход
        print(res.url) # Видим замену http на https
        print(res.history) # Видим редирект в истории

if __name__ == '__main__':
    unittest.main()
