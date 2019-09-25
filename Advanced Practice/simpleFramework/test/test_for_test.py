
def test_paste_delete_issue_jira(api):
    res = api.login() #Логинимся

    #Проверяем статус. В данном случае - проверку лучше делать через куку.
    #Куки под проверку: X-Seraph-LoginReason
    #Т.к на валидный и не валидный ввод - статус код: 200
    assert res.status_code == 200 
    #Создаём репорт под имя прокета и указываем исполнителя
    res = api.addIssue("WEBINAR","Alex_Tropp")
    #Проверяем код 201 - успешно создан
    assert res.status_code == 201
    #Перевод ответа в json для простого получения ключа id, переданного в ответе от сервера
    res_json = res.json()
    #Сохраняем значение ключа id
    issueID = res_json["id"]
    #Отправляем запрос на удаление репорта
    res = api.deleteIssue(issueID)
    #Проверяем успешное удаление. 204 - успешно удалили
    assert res.status_code == 204
