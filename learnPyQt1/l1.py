import sys
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


#创键一个应用程序
# app = QApplication([])
app = QApplication(sys.argv)

#创建一个小窗口部件
# window = QWidget()
# window.show()#Windows默认隐藏生成的窗口

#创建一个主窗口
window = QMainWindow()
window.show()



#启动事件循环
app.exec_()
