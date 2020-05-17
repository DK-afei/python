from PyQt5 import QtWidgets
from learnPyQt2.second import Ui_MainWindow
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.comboBox.addItem("First item")
        self.ui.comboBox.addItem("Second item")
        #选择一个item
        self.ui.comboBox.setCurrentIndex(1)
        self.ui.comboBox.setCurrentText("First item")

    #获取所有items
    def get_all_item(self):
        for i in range(self.ui.comboBox.count()):
            print(self.ui.comboBox.itemText(i))

app = QtWidgets.QApplication([])
applicaton = mywindow()
applicaton.get_all_item()
applicaton.show()
sys.exit(app.exec())