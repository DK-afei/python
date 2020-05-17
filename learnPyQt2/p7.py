from PyQt5 import QtWidgets
from learnPyQt2.third import Ui_MainWindow
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(2)
        self.ui.tableWidget.setRowCount(4)
        self.ui.pushButton.setText("clear")
        self.ui.pushButton.clicked.connect(self.clear)

    #清除表格里的内容
    def clear(self):
        self.ui.tableWidget.clear()

app = QtWidgets.QApplication([])
applicaton = mywindow()
applicaton.show()
sys.exit(app.exec())




#pyuic5 learnPyQt2/third.ui -o learnPyQt2/third.py 将.ui文件转换为.py文件