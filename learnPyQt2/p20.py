import sys
import learnPyQt2.fifteenth
from PyQt5.QtWidgets import QApplication, QMainWindow
#设置信号的信号与插槽
#pyuic5 learnPyQt2/fifteenth.ui -o learnPyQt2/fifteenth.py 将.ui文件转换为.py文件
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = learnPyQt2.fifteenth.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
