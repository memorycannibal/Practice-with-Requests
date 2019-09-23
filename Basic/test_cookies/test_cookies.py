import unittest
import requests

class TestCase(unittest.TestCase):

    def test_cookies(self):
        url = "https://httpbin.org/cookies"

        # Отпарвка куки через dic
        cookies = {'country':'Russia','city':'Moscow'}
        r = requests.get(url,cookies=cookies)
        print('Тест 1:')
        print(r.text)

        # Просмотр куков
        res = requests.get("https://google.com")
        print('Куки гугла:')
        print(res.cookies["1P_JAR"]+"\n")
        
        # Отправка куков через CookieJar

        coockiejar = requests.cookies.RequestsCookieJar()
        coockiejar.set("cookiejar","testing",domain="httpbin.org",path="/cookies")
        coockiejar.set("coo","foo",domain="httpbin.org",path="/cookies")
        req2 = requests.get(url,cookies=coockiejar)
        print('Тест 2:')
        print(req2.text)


if __name__ == '__main__':
    unittest.main()
