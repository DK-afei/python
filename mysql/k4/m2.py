import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123321', db='test')
cur = conn.cursor()
cur.execute("delete from webscans_users where username='xu_yu'")
conn.commit()
cur.close()
conn.close()
