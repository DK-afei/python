import sys
from PyQt5.QtWidgets import QMainWindow, QHBoxLayout, QPushButton, QApplication, QToolTip, QWidget
from PyQt5.QtGui import QFont
class TooltipForm(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setUI()


    #为控件添加提示信息
    def setUI(self):
        QToolTip.setFont(QFont('SansSerif', 12))
        self.setToolTip('今天是<b>星期五</b>')
        self.setWindowTitle('设置控件消息')
        self.setGeometry(300,300,200,200)
        self.button1 = QPushButton('我的按钮')
        self.button1.setToolTip('这是一个按钮，Are you ok？')

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = TooltipForm()
    main.show()

    sys.exit(app.exec_())