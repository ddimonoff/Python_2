from sqlalchemy import create_engine, inspect, text

from CreatingPage import Creating

db_connection_string = "postgresql://postgres:85436@localhost:5432/postgres"
db = create_engine(db_connection_string)
creatbas = Creating(db)

def test_insert_subject():
    print("\nНачало теста создания записи")
    creatbas.get_connection()
    #  Количество записей в базе subject
    len_before = creatbas.get_list()
    max_id = creatbas.select_max_id()
    #  Создание новой записи
    new_subject = "Test01"
    value_ins = {"new_name":new_subject}
    creatbas.insert_name(value_ins)
    len_after = creatbas.get_list()
    #  Проверка создания записи
    assert len_after == len_before + 1
    new_id = max_id + 1
    value_new_id = {"new_ID": new_id, "subject_title": new_subject}
    creatbas.create_id(value_new_id)
    #  Удаление записи
    del_id = creatbas.select_max_id()
    deleted_id = {"subject_id": del_id}
    creatbas.deleted_at(deleted_id)
    len_final = creatbas.get_list()
    assert len_final == len_before
    print("Проверка теста создания записи пройдена успешно")
