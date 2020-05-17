import sys
from PyQt5.QtWidgets import QApplication, QLabel, QMainWindow
from PyQt5.QtCore import Qt

# QMainWindow的子类来定制应用程序的主窗口
class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)

        self.setWindowTitle("My Awesome App")

        label = QLabel("This is a PyQt5 window!")

        # Qt具有许多自定义的小部件属性，此处为设置居中
        label.setAlignment(Qt.AlignCenter)

        # 设置窗口的中央部件，默认小部件将展开以占用窗口的所有空间
        self.setCentralWidget(label)


app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()