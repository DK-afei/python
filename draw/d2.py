from PyQt5 import QtGui, QtCore
from PyQt5.QtGui import QPainter, QBrush, QPen
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
    #画弧
    def paintEvent(self, event):
        painter = QPainter()
        painter.begin(self)
        painter.setRenderHint(QPainter.Antialiasing)
        painter.setPen(QtCore.Qt.green)
        painter.setBrush(QtCore.Qt.white)
        painter.drawArc(100, 70, 300, 300, 0*16, 90*16)
        # painter.drawArc(100, 70 ,300, 300, 0 * 16, 180 * 16)
        # painter.drawArc(100, 70, 300, 300, 0 * 16, -180 * 16)

        # painter.drawArc(100, 70, 300, 300, 90 * 16, 180 * 16)
        # painter.drawArc(100, 70, 300, 300, -90 * 16, 180 * 16)


App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())