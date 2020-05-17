from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import sys

class Window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Tutorial"
        self.top = 150
        self.left = 150
        self.width = 500
        self.height = 500
        self.InitWindow()
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    def paintEvent(self, event):
        painter = QPainter(self)
        pic = QPixmap("omg.jpg")
        painter.drawPixmap(self.rect(), pic)
        painter.setPen(QPen(Qt.red, 8))
        painter.drawRect(40, 40, 400, 200)

App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())