from PyQt5 import Qt
from PyQt5 import QtWidgets
from learnPyQt2.second import Ui_MainWindow
import sys

#pyuic5 learnPyQt2/second.ui -o learnPyQt2/second.py 将.ui文件转换为.py文件
#
class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self.btnClicked)
    #通过方法重写完成信号（事件）的覆盖
    def keyPressEvent(self, e):
        if e.key() == Qt.Key_F12:
            self.close()
    #按钮信号触发插槽事件
    def btnClicked(self):
        self.ui.label.setText("Clicked")


app = QtWidgets.QApplication([])
applicaton = mywindow()
applicaton.show()
sys.exit(app.exec())