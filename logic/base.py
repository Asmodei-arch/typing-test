import sqlite3

import constants


class Base:
    def __init__(self, filename=constants.DATA_BASE_NAME):
        self.connect = sqlite3.connect(filename)
        self.cursor = self.connect.cursor()

    def executeAndCommit(self, query, args):
        self.cursor.execute(query, args)
        self.connect.commit()

    def executeAndFetch(self, query, args):
        return self.cursor.execute(query, args).fetchall()
