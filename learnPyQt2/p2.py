from PyQt5 import QtWidgets, QtGui, QtCore
from learnPyQt2.first import Ui_MainWindow
import sys

#pyuic5 learnPyQt2/first.ui -o learnPyQt2/first.py 将.ui文件转换为.py文件
#变更字型、文字
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.label.setFont(QtGui.QFont('SansSerif', 30))
        self.ui.label.setGeometry(QtCore.QRect(10, 10, 200, 200))
        self.ui.label.setText("LikeGeeks")

app = QtWidgets.QApplication([])
applicaton = mywindow()
applicaton.show()
sys.exit(app.exec())