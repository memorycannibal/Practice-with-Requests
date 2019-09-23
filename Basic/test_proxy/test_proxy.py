import unittest
import requests

class TestCase(unittest.TestCase):

    def test_get(self):
        proxy = {"https":"200.255.122.170:8080"}

        res = requests.get("https://httpbin.org/ip",proxies=proxy)
        print(res.text)




if __name__ == '__main__':
    unittest.main()
