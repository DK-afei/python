# -*-coding:UTF-8-*-

import pymysql

try:
    #获取数据库连接
    conn = pymysql.connect(host='localhost',user='root',passwd='123321',db='test',port=3306,charset='utf8')
    #打印数据库连接对象
    print('数据库连接对象为：{}'.format(conn))
    # 获取游标
    cur = conn.cursor()

    # ----------删除数据-----------------------
    # sql="delete from pyTest"
    # try:
    #     cur.execute(sql)
    #     conn.commit()
    # except:
    #     conn.rollback()

    # ----------修改数据-----------------------
    # #写法1：sql="update pyTest set name='李四' where id='%s'" %('123')
    # #写法2：
    # sql = "update pyTest set name='王五' where id='123'"
    # try:
    #     cur.execute(sql)
    #     conn.commit()
    # except:
    #     conn.rollback()

    # ----------插入数据-----------------------
    # sql="insert into pyTest(id,name,sex)values('123','张三','男')"
    # try:
    #     #执行sql语句
    #     cur.execute(sql)
    #     #提交到数据库执行
    #     conn.commit()
    # except:
    #     #发生错误时回滚
    #     conn.rollback()

    # ----------创建表-----------------------
    # #如果表已经存在 则使用 execute()方法删除表
    # cur.execute("drop table if EXISTS  pyTest")
    # #创建表sql语句
    # sql="""create table pyTest (
    #       id VARCHAR(20) NOT NULL  PRIMARY KEY,
    #       name VARCHAR(20),
    #       sex CHAR(2)
    #     )"""
    # cur.execute(sql)


    #   ----------进行查询操作-----------------------
    #打印游标
    print("游标为：{}".format(cur))
    print("游标是：" + str(cur))
    #查询sql语句
    sql='select * from student'
    cur.execute(sql)
    conn.commit()
    #使用 fetchall() 方法获取数据对象,即是多条数据
    data = cur.fetchall()
    #使用 fetchone() 方法获取一条数据
    #data = cur.fetchone()
    for item in data:
        print(item)
    cur.close()
    conn.close()
except Exception as e:
            print(e)
