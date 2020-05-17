import sys
import learnPyQt2.thirteenth
from PyQt5.QtWidgets import QApplication, QMainWindow
#设置控件之间的伙伴关系
#pyuic5 learnPyQt2/thirteenth.ui -o learnPyQt2/thirteenth.py 将.ui文件转换为.py文件
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = learnPyQt2.thirteenth.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
