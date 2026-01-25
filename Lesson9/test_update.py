from sqlalchemy import create_engine, inspect, text

from UpdatingPage import Updating

db_connection_string = "postgresql://postgres:85436@localhost:5432/postgres"
db = create_engine(db_connection_string)
upbas = Updating(db)

def test_insert_subject():
    print("\nНачало теста корректировки записи")
    upbas.get_connection()
    #  Количество записей в базе teacher
    len_before = upbas.get_list()
    max_id = upbas.select_max_id()
    #  Создание новой записи
    new_email = "test02@ya.ru"
    value_ins = {"new_name":new_email}
    upbas.insert_name(value_ins)
    len_after = upbas.get_list()
    #  Проверка создания записи
    assert len_after == len_before + 1
    new_id = max_id + 1
    value_new_id = {"new_ID": new_id, "email": new_email}
    upbas.create_id(value_new_id)
    #  Удаление записи
    del_id = upbas.select_max_id()
    deleted_id = {"teacher_id": del_id}
    upbas.deleted_at(deleted_id)
    len_final = upbas.get_list()
    assert len_final == len_before
    print("Проверка теста корректировки записи пройдена успешно")
