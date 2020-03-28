import sqlite3
import pandas as pd
import os


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
        self.conn.close()

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data (answer TEXT, source TEXT, link TEXT)")
        self.conn.commit()

    def add_question(self, answer, source, link):
        insertion = (answer, source, link)

        self.cursor.execute("INSERT INTO data (answer, source, link) VALUES (?, ?, ?)", insertion)
        self.conn.commit()

    def get_answer(self, question):
        self.cursor.execute("SELECT answer, source FROM data")

        return self.cursor.fetchone()

    def delete(self, *args, all=False):
        if all:
            self.cursor.execute("DELETE FROM data")
        else:
            for _id in args:
                self.cursor.execute("DELETE FROM data WHERE id = (?)", (_id,))
        self.conn.commit()

    def print(self):
        print(pd.read_sql_query("SELECT * FROM data", self.conn))
