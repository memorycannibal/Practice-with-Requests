import requests

# Наша callback функция
def res_info(r,*arg,**kwarg):
    print(r.status_code, r.url)
    print(r.text)
# Наша callback функция
def res_heades(r,*arg,**kwarg):
    print(r.headers)

def test_event_hook():
    hook = {"response" : (res_info, res_heades )} # Инициализируем хук c кортежем из 2х коллбек функций
    req = requests.get("https://httpbin.org/get", hooks=hook) # Делаем запрос и ождиаем срабатывание хука при ответе от сервера

if __name__ == '__main__':
    test_event_hook()
