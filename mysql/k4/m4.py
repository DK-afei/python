import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123321', db='test')
cur = conn.cursor()
cur.execute('select * from student')
for users in cur.fetchall():
    print('用户名：', users[0], '密码：', users[1])
cur.close()
conn.close()
