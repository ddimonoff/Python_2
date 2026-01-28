from sqlalchemy import create_engine, inspect, text

from DeletingPage import Deleting

db_connection_string = "postgresql://postgres:85436@localhost:5432/postgres"
db = create_engine(db_connection_string)
delbas = Deleting(db)

def test_insert_subject():
    print("\nНачало теста удаления записи")
    delbas.get_connection()
    #  Количество записей в базе subject
    len_before = delbas.get_list()
    max_id = delbas.select_max_id()
    #  Создание новой записи
    new_user_email = "test03@mail.com"
    value_ins = {"new_name":new_user_email}
    delbas.insert_name(value_ins)
    len_after = delbas.get_list()
    #  Проверка создания записи
    assert len_after == len_before + 1
    new_id = max_id + 1
    value_new_id = {"new_ID": new_id, "user_email": new_user_email}
    delbas.create_id(value_new_id)
    #  Удаление записи
    del_id = delbas.select_max_id()
    deleted_id = {"user_id": del_id}
    delbas.deleted_at(deleted_id)
    len_final = delbas.get_list()
    assert len_final == len_before
    print("Проверка теста удаления записи пройдена успешно")
