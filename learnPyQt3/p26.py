'''

操作MySql数据库

'''
from PyQt5.QtSql import QSqlQuery
from PyQt5 import QtSql


def createDB():
    db = QtSql.QSqlDatabase.addDatabase('QMYSQL')
    db.setHostName('localhost')
    db.setPort(3306)
    db.setDatabaseName('test')
    db.setUserName('root')
    db.setPassword('123321')

    if not db.open():
        print('无法建立与数据库的连接！')
        return False
    else:
        print('连接成功！')
        query = QSqlQuery()
        try:
            query.exec('insert into pytest (id, name, sex) values ("789", "王二", "男")')
            print('mysql语句执行完毕！')
        except:
            print('执行失败')
        db.close()
        return True

if __name__ == '__main__':
    print(QtSql.QSqlDatabase.drivers())
    createDB()