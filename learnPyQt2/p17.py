import sys
import learnPyQt2.twelve
from PyQt5.QtWidgets import QApplication, QMainWindow
#尺寸策略
#pyuic5 learnPyQt2/twelve.ui -o learnPyQt2/twelve.py 将.ui文件转换为.py文件
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = learnPyQt2.twelve.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
