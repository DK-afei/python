import sys
import learnPyQt2.sixth
from PyQt5.QtWidgets import QApplication, QMainWindow
#水平、垂直布局的综合应用
#pyuic5 learnPyQt2/sixth.ui -o learnPyQt2/sixth.py 将.ui文件转换为.py文件
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = learnPyQt2.sixth.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
