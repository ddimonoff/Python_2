from sqlalchemy import create_engine, inspect, text


class Updating:

    __scripts = {
        "select": text("SELECT * FROM teacher"),
        "select_max_id": text("SELECT MAX(teacher_id) FROM teacher"),
        "select_new": text("SELECT teacher_id FROM teacher WHERE teacher.email = :email"),
        "delete_by_id": text("DELETE FROM teacher WHERE teacher.teacher_id = :teacher_id"),
        "insert_new": text("INSERT INTO teacher(\"email\") VALUES (:new_name)"),
        "create_id": text("UPDATE teacher SET teacher_id = :new_ID WHERE teacher.email = :email")
    }

    def __init__(self, db) -> None:
        self.__db = db

    def get_connection(self):
        inspector = inspect(self.__db)
        res = inspector.get_table_names()
        assert res[2] == 'student'

    def get_list(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select"])
        rows = len(result.mappings().all())
        conn.close()
        return rows

    def insert_name(self, value):
        conn = self.__db.connect()
        transaction = conn.begin()
        conn.execute(self.__scripts["insert_new"], value)
        transaction.commit()
        conn.close()

    def select_max_id(self):
        conn = self.__db.connect()
        result = conn.execute(self.__scripts["select_max_id"])
        conn.close()
        return result.fetchone()[0]

    def select_name(self, value):
        conn = self.__db.connect()
        transaction = conn.begin()
        new_id = conn.execute(self.__scripts["select_new"], value)
        transaction.commit()
        conn.close()
        return new_id.fetchone()[0]

    def create_id(self, value):
        conn = self.__db.connect()
        transaction = conn.begin()
        conn.execute(self.__scripts["create_id"], value)
        transaction.commit()
        conn.close()

    def deleted_at(self, value):
        conn = self.__db.connect()
        transaction = conn.begin()
        conn.execute(self.__scripts["delete_by_id"], value)
        transaction.commit()
        conn.close()
