import sys
import learnPyQt2.seventh
from PyQt5.QtWidgets import QApplication, QMainWindow
#栅格布局
#pyuic5 learnPyQt2/seventh.ui -o learnPyQt2/seventh.py 将.ui文件转换为.py文件
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = learnPyQt2.seventh.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
