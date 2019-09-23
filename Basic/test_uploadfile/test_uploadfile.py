import unittest
import requests

class TestCase(unittest.TestCase):

    def test_upload(self):
       
        #files = {"file": open("text.txt","rb")} - Для одного файла
        files =[ 
            ("file",('test.txt',open('test.txt','rb'),'txt')) ,
            ("file2",('test2.txt',open('test2.txt','rb'),'txt'))
        ]
        res = requests.post("http://httpbin.org/post",files=files)
        print(res.text)



if __name__ == '__main__':
    unittest.main()