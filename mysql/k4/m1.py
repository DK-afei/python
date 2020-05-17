import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123321', db='test')
cur = conn.cursor()
cur.execute("insert into webscans_users values ('liu_hua','vfd6811dw')")
conn.commit()
cur.close()
conn.close()
