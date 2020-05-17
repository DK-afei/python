import sys
from PyQt5.QtWidgets import QHBoxLayout, QPushButton, QMainWindow, QApplication, QWidget

class QuitApplication(QMainWindow):
    def __init__(self):
        super(QuitApplication, self).__init__()
        self.setWindowTitle('退出应用程序')
        self.resize(300, 120)
        #添加Button
        self.button1 = QPushButton('退出应用程序')
        #将信号与槽关联
        self.button1.clicked.connect(self.onClick_Button)

        layout = QHBoxLayout()
        layout.addWidget(self.button1)

        mainFrame = QWidget()
        mainFrame.setLayout(layout)
        self.setCentralWidget(mainFrame)
    #按钮事件单击的方法
    def onClick_Button(self):
        sender = self.sender()
        print(sender.text()+'clicked!')
        app = QApplication.instance()
        #退出应用程序
        app.quit()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QuitApplication()
    main.show()
    sys.exit(app.exec_())
