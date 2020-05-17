import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from PyQt5.QtGui import QIcon

class FirstMainWin(QMainWindow):
    def __init__(self):
        super(FirstMainWin, self).__init__()
        self.setUi()

    def setUi(self):
        #设置主窗口的标题
        self.setWindowTitle('设置窗口图标')
        #设置窗口尺寸及窗口大小
        self.setGeometry(300,300,250,250)

        #设置窗口的图标
        self.setWindowIcon(QIcon('omg.jpg'))



if __name__ == '__main__':
    app = QApplication(sys.argv)
    #app.setWindowIcon(QIcon('omg.jpg'))
    main = FirstMainWin()
    main.show()

    sys.exit(app.exec_())

