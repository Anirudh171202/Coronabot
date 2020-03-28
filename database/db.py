import sqlite3
import pandas as pd
import os
from json import dump, load

class Database:
    def __init__(self, path, *args, **kwargs):
        self.path = path
        self.connect()
        # hist ={
        #     [word]: {
        #          count: number,
        #          index:  number[]
        #     }
        # }
        try:
            self.hist = load(open("histogram.json", "w+"))
        except:
            self.hist = {}
        self._length = 0

    @property
    def length(self):
        return self._length
        
    def __del__(self):
        print(self)
        # dump(self.hist, open("histogram.json", "w+"))
        self.disconnect()

    def connect(self):
        self.conn = sqlite3.connect(os.path.join(
            os.getcwd(), self.path))
        self.cursor = self.conn.cursor()
        try: 
            self._length = len(self.all())
        except:
            self._length = 0

    def disconnect(self):
        self.cursor.close()
        self.conn.close()

    def from_csv(self, path):
        df = pd.read_csv(path)[["User", "Tweet", "Permalink"]]
        # df.columns = ["source", "answer", "link"]
        print("Loading csv into db");
        df.rename(columns = {
            "User": "source",
            "Tweet": "answer",
            "Permalink": "link"
            }, inplace=True)
        df.to_sql("data", self.conn, if_exists="append", index=True)

        self._length = len(self.all())

        print("Creating histogram")
        self.create_hist()
        # print("\n", self.hist)

    def create_table(self):
        self.cursor.execute("CREATE TABLE IF NOT EXISTS data (index INT, answer TEXT, source TEXT, link TEXT)")
        self.conn.commit()

    def add(self, answer, source, link):
        insertion = (answer, source, link)
        self.add_hist(answer, self._length)
        self._length += 1
        self.cursor.execute("INSERT INTO data (index, source, link) VALUES (?, ?, ?)", insertion)
        self.conn.commit()

    def all(self):
        return self.cursor.execute("SELECT * FROM data").fetchall()

    def add_hist(self, string, index):
        text = string.split()
        for i in text:
            if  self.hist.get(i) != None:
                self.hist[i]  += 1
            else:
                self.hist[i] = 1

    def create_hist(self):
        for (index,  _, answer, __,) in self.all():
            a = int(index / self._length * 100)
            print("\r[" + ("#" * a) + (" " * (100 - a)) + "]       ", index, end="       ")
            self.add_hist(answer, index)
            
        dump(self.hist, open("histogram.json", "w+"))


    def search(self, query):
        pass

    def delete(self, *args, all=False):
        if all:
            self.cursor.execute("DELETE FROM data")
        else:
            for _id in args:
                self.cursor.execute("DELETE FROM data WHERE id = (?)", (_id,))
        self.conn.commit()

    def print(self):
        print(pd.read_sql_query("SELECT * FROM data", self.conn))
