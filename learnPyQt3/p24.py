from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Toolbar(QMainWindow):
    def __init__(self):
        super(Toolbar, self).__init__()
        self.setUI()
    def setUI(self):
        self.setWindowTitle("工具栏例子")
        self.resize(300,200)
        tb1 = self.addToolBar("File")
        new = QAction(QIcon('omg.jpg'),"new",self)
        tb1.addAction(new)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = Toolbar()
    main.show()
    sys.exit(app.exec_())
