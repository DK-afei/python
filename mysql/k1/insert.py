# coding=utf-8

import pymysql


# 插入操作
def inser_A():
    conn = pymysql.connect(host='localhost', user='root', password='123321', db='test', port=3306, charset='utf8')

    cur = conn.cursor()

    sql_insert = "insert into student values ('1608110148', 'ZhuShiYuan', 18)"

    cur.execute(sql_insert)

    conn.commit()

    cur.close()

    conn.close()


# 带信息查重的插入操作
def insert_B(ID, Name, Age):
    conn = pymysql.connect(host='localhost', user='root', password='123321', db='test', port=3306, charset='utf8')

    cur = conn.cursor()

    sql_insert = "insert into student values ('%s', '%s', %d)" % (ID, Name, Age)

    sql_query = "select count(*) from student where studentID = '%s'" % (ID)

    cur.execute(sql_query)

    conn.commit()

    data = cur.fetchone()

    if data[0] == 1:

        print("信息已存在, 不可重复插入")

    else:

        cur.execute(sql_insert)

        conn.commit()

    cur.close()

    conn.close()