import sys
import learnPyQt2.ninth
from PyQt5.QtWidgets import QApplication, QMainWindow
#容器布局
#pyuic5 learnPyQt2/ninth.ui -o learnPyQt2/ninth.py 将.ui文件转换为.py文件
if __name__ == '__main__':
    app = QApplication(sys.argv)
    mainWindow = QMainWindow()
    ui = learnPyQt2.ninth.Ui_MainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
