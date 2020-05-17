import sys
import learnPyQt2.fifth
from PyQt5.QtWidgets import QApplication, QMainWindow
#垂直布局
#pyuic5 learnPyQt2/fifth.ui -o learnPyQt2/fifth.py 将.ui文件转换为.py文件
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = learnPyQt2.fifth.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())




