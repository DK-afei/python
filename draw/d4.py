from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPainter, QBrush, QPen, QPainterPath
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QApplication, QMainWindow
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
    #画矩形
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.setPen(QPen(Qt.black, 5, Qt.DotLine))
        # painter.setPen(QPen(Qt.black, 5, Qt.SolidLine))
        painter.setBrush((QBrush(Qt.yellow, Qt.SolidPattern)))
        painter.drawRect(40, 40, 400, 200)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())