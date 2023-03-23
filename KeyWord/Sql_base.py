# -*- coding:utf-8 -*-
# @Time  :2023/3/24 1:52
# @AUTHOR:希耶谢

'''
数据库连接
SQL语句执行操作
'''

import pymysql

DictCursor = pymysql.cursors.DictCursor


class Sql:

    def __init__(self, host, port, user, password, database):
        self.db = pymysql.connect(
            host=host,
            port=port,  # 端口--->int类型
            user=user,
            password=password,
            database=database
        )

        self.__cursor = self.db.cursor(DictCursor)  # 游标对象

    def execute(self, sql):
        """执行数据库语句"""
        self.__cursor.execute(sql)
        return self

    # 获取一条查询结果
    def fetchone(self):
        return self.__cursor.fetchone()

    # 获取全部查询结果
    def fetchall(self):
        return self.__cursor.fetchall()


# if __name__ == '__main__':
#     Sql.execute(sql).fetchone()
