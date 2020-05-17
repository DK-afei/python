import sys
import learnPyQt2.fourth
from PyQt5.QtWidgets import QApplication, QMainWindow
#水平布局
#pyuic5 learnPyQt2/fourth.ui -o learnPyQt2/fourth.py 将.ui文件转换为.py文件

if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = learnPyQt2.fourth.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())