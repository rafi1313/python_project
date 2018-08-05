import pymysql


class DBConnect:
    def __init__(self):
        # self.query = _query
        self.conn = pymysql.connect('localhost', 'root', 'SqlAccount!23', 'DMP', charset='utf8')
        self.c = self.conn.cursor()

    def execute(self, _query):
        self.c.execute(_query)

    def fetchAll(self, _query):
        self.c.execute(_query)
        return self.c.fetchall()
