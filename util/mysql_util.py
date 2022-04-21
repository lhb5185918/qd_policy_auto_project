from config.database import db
from util.read_case import get_case
import pymysql
class Pysql_util:
    def __init__(self):
        self.ob = db.cursor(cursor=pymysql.cursors.DictCursor)

    def singal_select(self,sql):
        try:
            self.ob.execute(sql)
        except:
            print("sql执行失败")
            db.rollback()
        return self.ob.fetchone()

    def more_select(self,sql):
        try:
            self.ob.execute(sql)
        except:
            print("sql执行失败")
            db.rollback()
        return self.ob.fetchone()

    def insert(self,sql):
        try:
            self.ob.execute(sql)
        except:
            print("sql执行失败")
            db.rollback()
        return self.ob.fetchone()

    @classmethod
    def close(cls):
        db.close()

