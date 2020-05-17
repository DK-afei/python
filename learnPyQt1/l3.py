import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

# QMainWindow的子类来定制应用程序的主窗口
class MainWindow(QMainWindow):
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        #四个信号，并且与对应的插槽相绑定
        self.windowTitleChanged.connect(self.onWindowTitleChange)

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn())

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x))

        self.windowTitleChanged.connect(lambda x: self.my_custom_fn(x, 25))
        # 设置窗口标题，触发所有上述信号
        self.setWindowTitle("My Awesome App")

        label = QLabel("THIS IS AWESOME!!!")
        label.setAlignment(Qt.AlignCenter)

        self.setCentralWidget(label)
    #插槽；接受字符串，例如窗口标题
    def onWindowTitleChange(self, s):
        print(s)
    #插槽：具有默认参数，可以不带值
    def my_custom_fn(self, a="HELLLO!", b=5):
        print(a, b)

app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()