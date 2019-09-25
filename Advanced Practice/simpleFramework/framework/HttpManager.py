import requests
import json
import urllib3

class HttpManager:
    
    #Переменные для хранения хидеров и куков
    Headers = {'Content-Type': 'application/json'}
    Cookies = {}
    

    #Убираем предупреждения о том, что у нас отключена проверка сертификата
    def __init__(self):
        urllib3.disable_warnings()

    #Хук на обновление куков. Можно было добавить в тело методов, но так, думаю, лучше
    #т.к может пригодиться в разных функциях
    def event_hook(self,r,*arg,**kwarg):
        self.Cookies = r.cookies

    #Отправка обычного поста с данными в url, сохранением куков, установкой хидеров и отключение проверки сертификата
    def post(self,url,data= {}):
        hook = {"response": self.event_hook}
        return requests.post(url,verify=False,params=data,cookies=self.Cookies,headers=self.Headers,hooks=hook)
    
    #Отправка json через post c сохранением куков, установкой хидеров и отключение проверки сертификата
    def postJson(self,url,jsonObject):
        return requests.post(url,verify=False,data=json.dumps(jsonObject),headers=self.Headers,cookies=self.Cookies)

    #Обычный get c указанием куков, установкой хидеров и отключение проверки сертификата
    #Также принимает данные для вставки в url
    def get(self,url,args={}):
        return requests.get(url,paramas=args,verify=False,headers=self.Headers,cookies=self.Cookies)

    #Отпрака Delete на указанный url с указанием куков, установкой хидеров и отключение проверки сертификата
    def delete(self,url):
        return requests.delete(url,verify=False,headers=self.Headers,cookies=self.Cookies)