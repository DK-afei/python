import sys
import learnPyQt2.eleventh
from PyQt5.QtWidgets import QApplication, QMainWindow
#分割线与间隔(期望尺寸)
#pyuic5 learnPyQt2/eleventh.ui -o learnPyQt2/eleventh.py 将.ui文件转换为.py文件
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = learnPyQt2.eleventh.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
