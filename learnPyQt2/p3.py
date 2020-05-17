from PyQt5 import QtWidgets, QtCore
from learnPyQt2.first import Ui_MainWindow
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.lineEdit.setText("Welcome to LikeGeeks website")
        self.ui.lineEdit_2.setMaxLength(10)
        self.ui.lineEdit_3.setEchoMode(QtWidgets.QLineEdit.Password)
        self.ui.lineEdit_4.setReadOnly(True)
        self.ui.lineEdit_5.setStyleSheet("color: rgb(28, 43, 255);")
        self.ui.lineEdit_6.setStyleSheet("background-color: rgb(28, 43, 255);")

app = QtWidgets.QApplication([])
applicaton = mywindow()
applicaton.show()
sys.exit(app.exec())