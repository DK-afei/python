import sys
import learnPyQt2.tenth
from PyQt5.QtWidgets import QApplication, QMainWindow
#绝对布局
#pyuic5 learnPyQt2/tenth.ui -o learnPyQt2/tenth.py 将.ui文件转换为.py文件
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = learnPyQt2.tenth.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
