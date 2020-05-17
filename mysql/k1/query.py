# coding=utf-8

import pymysql


# 查询操作
def select():
    conn = pymysql.connect(host='localhost', user='root', password='123321', db='test', port=3306, charset='utf8')

    cur = conn.cursor()

    sql = "select * from student"

    cur.execute(sql)

    conn.commit()

    data = cur.fetchall()

    for item in data:
        print(item)

    cur.close()

    conn.close()
