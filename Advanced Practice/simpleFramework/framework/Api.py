from simpleFramework.framework.HttpManager import HttpManager
from simpleFramework.framework.Jsonfix import reportTemplate

class Api:
    #Данные под авторизацию
    authValue = {"os_username":"webinar5",
                 "os_password":"webinar5"}

    #Переменная под id созданного репорта 
    createdIssueID = None

    #Создаём объект httpManager на автомате
    def __init__(self):
        self.httpManager = HttpManager()

    #Функция логина
    def login(self):
        return self.httpManager.post("https://jira.hillel.it/login.jsp",self.authValue)
        
    #Добавляем репорт в jira с указанием проекта и девелопера для исправления
    def addIssue(self,key,assignee):
        jsonObject = reportTemplate.for_create_issue(key,assignee)
        return self.httpManager.postJson("https://jira.hillel.it/rest/api/2/issue/",jsonObject)
       
    #Удаляем репорт по его id
    def deleteIssue(self,issueID):
        return self.httpManager.delete("https://jira.hillel.it/rest/api/2/issue/{}".format(issueID))
        