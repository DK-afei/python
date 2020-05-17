import sys
from PyQt5.QtWidgets import QMainWindow, QLabel, QApplication, QToolTip, QWidget, QVBoxLayout
from PyQt5.QtGui import QPalette, QPixmap
from PyQt5.QtCore import Qt


class QlabelDemo(QWidget):
    def __init__(self):
        super().__init__()
        self.setUI()
    #QLabel的基本使用方法
    def setUI(self):
        label1 = QLabel(self)
        label2 = QLabel(self)
        label3 = QLabel(self)
        label4 = QLabel(self)

        label1.setText("<font color=yellow>this is a text label</font>")
        label1.setAutoFillBackground(True)

        palette = QPalette()#调色板
        palette.setColor(QPalette.Window,Qt.blue)#设置背景色
        label1.setPalette(palette)
        label1.setAlignment(Qt.AlignCenter)

        label2.setText("<a href='#'>welcome to my python GUI</a>")

        label3.setAlignment(Qt.AlignCenter)
        label3.setToolTip('this a picture label')
        label3.setPixmap(QPixmap("omg.jpg"))
        #如果设为True，则可以用浏览器打开网页，否则调用槽函数
        label4.setOpenExternalLinks(True)
        label4.setText("<a href='http://www.baidu.com'>baidu.com</a>")
        label4.setAlignment(Qt.AlignRight)
        label4.setToolTip('这是一个超级链接！')

        vbox = QVBoxLayout()
        vbox.addWidget(label1)
        vbox.addWidget(label2)
        vbox.addWidget(label3)
        vbox.addWidget(label4)


        label2.linkHovered.connect(self.linkHovered)
        label4.linkActivated.connect(self.linkClicked)
        self.setLayout(vbox)
        self.setWindowTitle('QLabel控件演示')
    def linkHovered(self):
        print('当鼠标滑过label2标签时候，触发事件')

    def linkClicked(self):
        print('当鼠标单机label4标签时，触发事件')



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlabelDemo()
    main.show()
    sys.exit(app.exec_())