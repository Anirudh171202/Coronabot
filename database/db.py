import sqlite3
import pandas as pd
import os
from json import dump, load


class Database:

    thresh_count = 100
    max_num_entries = 10

    def __init__(self, path, *args, **kwargs):
        self.path = path
        self.connect()
        '''
        Schema for hist: 
        hist = {
            [word]: {
                count: number,
                index:  number[]
            }
        }
        '''

        try:
            self.hist = load(open("histogram.json", "w+"))
        except:
            self.hist = {}
        self._length = 0

    def __del__(self):
        with open("histogram.json", "w+", encoding='utf-8-sig') as f:
            dump(self.hist, f)
            f.close()
        self.disconnect()

    @property
    def length(self):
        return self._length

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
        print("Loading csv into db")

        df = pd.read_csv(path)[["User", "Tweet", "Permalink"]]
        df["id"] = pd.Series(df.index, index=df.index)

        columns = df.columns.tolist()[:]
        columns.insert(0, columns.pop())
        df = df[columns]

        df.rename(columns={
            "User": "source",
            "Tweet": "answer",
            "Permalink": "link"
        }, inplace=True)
        df.to_sql("data", self.conn, if_exists="append", index=False)

        self._length = len(self.all())

        print("Creating histogram")
        self.create_hist()

    def create_table(self):
        self.cursor.execute(
            "CREATE TABLE IF NOT EXISTS data (id INT, answer TEXT, source TEXT, link TEXT)")
        self.conn.commit()

    def create_hist(self):
        for (index, _, answer, _,) in self.all():
            a = int(index / self._length * 100)
            print("\r[" + ("#" * a) + (" " * (100 - a)) +
                  "]       ", index, end="       ")
            self.add_hist(answer, index)

        print()
        with open("histogram.json", "w+", encoding='utf-8-sig') as f:
            dump(self.hist, f)
            f.close()

    def add_hist(self, string, index):
        text = string.split()
        for word in text:
            word = word.lower()
            if not word.isalnum():
                continue
            if self.hist.get(word) != None:
                self.hist[word]['count'] += 1
                self.hist[word]['index'].append(index)
            else:
                self.hist[word] = {'count': 1, 'index': [index]}

    def search(self, query):
        text = query.split()
        scores = {}
        for word in text:
            word = word.lower()
            if self.hist.get(word) == None:
                continue
            count, indices = list(self.hist[word].values())
            if count > self.thresh_count:
                continue
            for i in indices:
                if scores.get(i) == None:
                    scores[i] = 0
                scores[i] += 1/count
        top_entry_indices = sorted(scores.items(), key=lambda x: x[1])[
            :self.max_num_entries]

        top_entries = [self.get(i) for i, s in top_entry_indices]

        return top_entries

    def get(self, index):
        self.cursor.execute(
            f"SELECT answer, link FROM data WHERE id = (?)", (index,))
        return self.cursor.fetchone()[0]

    def all(self):
        return self.cursor.execute("SELECT * FROM data").fetchall()

    def add(self, answer, source, link):
        insertion = (answer, source, link)
        self.add_hist(answer, self._length)
        self._length += 1
        self.cursor.execute(
            "INSERT INTO data (id, source, link) VALUES (?, ?, ?)", insertion)
        self.conn.commit()

    def delete(self, *args, all=False):
        if all:
            self.cursor.execute("DELETE FROM data")
        else:
            for _id in args:
                self.cursor.execute(
                    "DELETE FROM data WHERE id = (?)", (_id,))
        self.conn.commit()

    def print(self):
        print(pd.read_sql_query("SELECT * FROM data", self.conn))
