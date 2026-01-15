from NegPage import NegPage


base_url =  "https://ru.yougile.com/api-v2"

my_headers = {}
my_headers["Authorization"] = API_KEY
my_headers["Content-Type"] = "application/json; charset=utf-8"
project_id = "3ea2b983-164b-4a83-9ec8-09f3d939b99"


def test_negative_yougile():

    negpage = NegPage(base_url)

    # некорректный Bearer при запросе списка проектов
    neg_key = API_KEY[8:]
    negpage.get_projects_list(neg_key)

    # некорректная роль при создании проекта
    project_new ={
        "title": "ДРЗЧ",
        "users": {"86368900-b3ab-4f67-8b99-75c8bd01189f": "guest"}
    }
    negpage.create_project(project_new, my_headers)

    # Пустое наименование при корректировке проекта
    project_new = {
        "title": "ДРЗЧ",
        "users": {"86368900-b3ab-4f67-8b99-75c8bd01189f": "admin"}
    }
    negpage.modify_project(project_new, my_headers)

    # Поиск проекта по некорректному ID
    negpage.get_project(project_id, my_headers)
