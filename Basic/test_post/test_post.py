import unittest
import requests

class TestCase(unittest.TestCase):

    def test_get(self):

         payload = {"email":"eve.holt@reqres.in","password":"pistol"}
         res = requests.post('https://reqres.in/api/register',payload)
         self.assertEqual(res.status_code,200)
         res = res.json()
         print("Id: {}. toked: {}.".format(res["id"],res["token"]))      


         payload = {"name":"morpheus","job":"leader"}
         res = requests.post('https://reqres.in/api/users/',payload)
         self.assertEqual(res.status_code,201)
         res = res.json()
         print("User: {}. Job: {}. Created: {}".format(res["name"],res["job"],res["createdAt"]))       






if __name__ == '__main__':
    unittest.main()