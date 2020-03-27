import sqlite3
import pandas as pd


class Database:
    def __init__(self, path, *args, **kwargs):
        self.path = path
        self.connect()

    def __del__(self):
        self.disconnect()

    def connect(self):
        self.conn = sqlite3.connect(os.path.join(
            os.getcwd(), self.path))
        self.cursor = self.conn.cursor()

    def disconnect(self):
        self.cursor.close()
        self.self.conn.close()

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS queue (id INT, qjson TEXT, ajson TEXT, status INT)")
        self.conn.commit()

    def add_question(self, question, _id):
        insertion = (question, _id, 0)

        self.cursor.execute(
            "INSERT INTO queue (qjson, id, status) VALUES (?, ?, ?)", insertion)
        self.conn.commit()

    def add_answer(self, answer, status, _id):
        insertion = (answer, status, _id)

        self.cursor.execute(
            "UPDATE queue SET (ajson) = (?), (status) = (?) WHERE id = (?)", insertion)
        self.conn.commit()

    def get_answer(self, _id):
        self.cursor.execute("SELECT ajson FROM queue WHERE id = (?)", (_id,))

        a = self.cursor.fetchone()[0]

        return parse(a)

    def get_status(self, _id):
        self.cursor.execute("SELECT status FROM queue WHERE id = (?)", (_id,))

        a = self.cursor.fetchone()[0]
        return a

    def delete(self, *args, all=False):
        if all:
            self.cursor.execute("DELETE FROM queue")
        else:
            for _id in args:
                self.cursor.execute("DELETE FROM queue WHERE id = (?)", (_id,))
        self.conn.commit()

    def print(self):
        print(pd.read_sql_query("SELECT * FROM queue", self.conn))
