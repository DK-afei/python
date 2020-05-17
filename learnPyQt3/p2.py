import sys
from PyQt5.QtWidgets import QDesktopWidget, QApplication, QMainWindow

class CenterForm(QMainWindow):
    def __init__(self):
        super(CenterForm, self).__init__()
        #设置主窗口的标题
        self.setWindowTitle('一个主窗口应用')
        #设置窗口的尺寸
        self.resize(400, 300)
    #窗口剧中显示
    def center(self):
        #设置屏幕坐标系
        screen = QDesktopWidget().screenGeometry()
        #获取窗口坐标系
        size = self.geometry()
        newLeft = (screen.width()-size.width())/2
        newTop = (screen.height()-size.height())/2

        self.move(newLeft,newTop)



if __name__ == '__main__':
    app = QApplication(sys.argv)

    main = CenterForm()
    main.show()

    sys.exit(app.exec_())

