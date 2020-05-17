from PyQt5.QtCore import pyqtSignal, QObject

#如何发出信号
class nut(QObject):
    cracked = pyqtSignal()
    def __init__(self):
        QObject.__init__(self)
    def crack(self):
        self.cracked.emit()

#如何使用信号
def crackit():
    print("hazelnut cracked!")

hazelnut = nut()
hazelnut.cracked.connect(crackit)
hazelnut.crack()