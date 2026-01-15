from PosPage import PosPage


base_url =  "https://ru.yougile.com/api-v2"

my_headers = {}
my_headers["Authorization"] = API_KEY
my_headers["Content-Type"] = "application/json; charset=utf-8"


def test_positive_yougile():
    pospage = PosPage(base_url)

    # Получить исходное количество проектов
    len_before = pospage.get_projects_list(my_headers)

    # # Создать новый проект
    project_new = {
        "title": "ДРЗЧ",
        "users": {"86368900-b3ab-4f67-8b99-75c8bd01189f": "admin"}
    }
    project_id = pospage.create_project(project_new, my_headers)
    project_title = project_new["title"]

    # Проверяем добавление нового проекта
    len_after = pospage.get_projects_list(my_headers)
    assert len_after - len_before == 1

    # Получить проект по ИД
    name_project = pospage.get_project(my_headers, project_id)
    assert name_project == project_title

    # # Скорректировать название проекта
    modified_project= {
        "title": "ДРЗЧ Отдел методологии",
    }
    pospage.modify_project(project_id, modified_project, my_headers)

    #  Проверка изменения названия проекта
    name_modify_project = pospage.get_project(my_headers, project_id)
    assert name_modify_project == modified_project["title"]

    pospage.delete_project(project_id, my_headers)

    len_finished = pospage.get_projects_list(my_headers)
    assert len_finished == len_before

    # print("")
    # print("Проектов было :", len_before)
    # print("Проектов стало :", len_after)
    # print("ID нового проекта:", project_id)
    # print("Новый проект называется:", name_project)
    # print("Название проекта изменено на:", name_modify_project)
    # print("После удаления проектов осталось:", len_finished)
