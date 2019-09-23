import unittest
import requests

class TestCase(unittest.TestCase):

    def test_handle_error(self):
        res = requests.get("https://httpbin.org/status/200",timeout=0.2)
        res.raise_for_status()

if __name__ == '__main__':
    unittest.main()
