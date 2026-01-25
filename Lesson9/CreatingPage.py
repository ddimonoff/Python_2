from sqlalchemy import create_engine, inspect, text


class Creating:

    __scripts = {
        "select": text("SELECT * FROM subject"),
        "select_max_id": text("SELECT MAX(subject_id) FROM subject"),
        "select_new": text("SELECT subject_id FROM subject WHERE subject.subject_title = :subject_title"),
        "delete_by_id": text("DELETE FROM subject WHERE subject.subject_id = :subject_id"),
        "insert_new": text("INSERT INTO subject(\"subject_title\") VALUES (:new_name)"),
        "create_id": text("UPDATE subject SET subject_id = :new_ID WHERE subject.subject_title = :subject_title")
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

