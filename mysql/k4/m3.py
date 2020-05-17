import pymysql
conn = pymysql.connect(host='localhost', port=3306, user='root', password='123321', db='test')
cur = conn.cursor()
cur.execute("update webscans_users set password='666666' where username='li_ming'")
conn.commit()
cur.close()
conn.close()
