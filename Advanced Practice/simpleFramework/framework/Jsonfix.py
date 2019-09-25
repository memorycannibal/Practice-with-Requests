class reportTemplate:
    
    '''
    Шаблон под отправку репорта в jira
    Каждое поле можно объявить в качестве переменной по тойже схеме
    '''

    @staticmethod
    def for_create_issue(projectKey,assignee):
        json = {
            "fields": {
                "project":
                    {
                        "key": projectKey
                    },
                "summary": "Test Summary",
                "description": "Creating of an issue",
                "assignee": {"name": assignee},
                "priority": {"name": "High"},
                "issuetype": {"name": "Test"}
            }
        }
        return json