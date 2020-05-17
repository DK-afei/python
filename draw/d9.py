from PyQt5 import QtGui
from PyQt5.QtGui import QPainter, QBrush, QPen, QColor, QFont
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.title = "PyQt5 Drawing Tutorial"
        self.top = 150
        self.left = 150
        self.width = 500
        self.height = 500
        self.InitWindow()
        self.text = "Python从菜鸟到高手"
    def InitWindow(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.top, self.left, self.width, self.height)
        self.show()
    def paintEvent(self, event):
        painter = QPainter(self)
        painter.begin(self)
        print('the window has changed!')
        painter.setPen(QColor(150, 43, 5))
        painter.setFont(QFont('SimSum', 25))
        painter.drawText(event.rect(), Qt.AlignCenter, self.text)
        painter.end()
App = QApplication(sys.argv)
window = Window()
sys.exit(App.exec())