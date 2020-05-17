import sys
import learnPyQt2.forteenth
from PyQt5.QtWidgets import QApplication, QMainWindow
#设置控件的tab顺序
#pyuic5 learnPyQt2/forteenth.ui -o learnPyQt2/forteenth.py 将.ui文件转换为.py文件
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = learnPyQt2.forteenth.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
