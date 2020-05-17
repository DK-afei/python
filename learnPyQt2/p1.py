from PyQt5 import QtWidgets, uic
import sys


#Python代码加载.ui文件
app = QtWidgets.QApplication([])
win = uic.loadUi("third.ui")
win.show()
sys.exit(app.exec())