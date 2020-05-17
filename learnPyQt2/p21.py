import sys
import learnPyQt2.sixteenth
from PyQt5.QtWidgets import QApplication, QMainWindow
#设计菜单和工具栏
#pyuic5 learnPyQt2/sixteenth.ui -o learnPyQt2/sixteenth.py 将.ui文件转换为.py文件
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = learnPyQt2.sixteenth.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
