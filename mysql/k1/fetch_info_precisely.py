# coding=utf-8

import pymysql


# 获取某一列信息
def fetch():
    conn = pymysql.connect(host='localhost', user='root', password='123321', db='test', port=3306, charset='utf8')

    cur = conn.cursor()

    sql = "select * from student"

    cur.execute(sql)

    conn.commit()

    data = cur.fetchall()

    for item in data:

        # 将姓名为'WangZiYuan'的ID号码输出

        if item[1] == "ZhuShiYuan":
            print(item[0])

    for item in data:

        # 将ID号为'12345'的姓名输出

        if item[0] == "1608110122":
            print(item[1])