from PyQt5.QtWidgets import *
import sys

class QlineEditEchoMode(QWidget):
    def __init__(self):
        super(QlineEditEchoMode, self).__init__()
        self.setUI()

    #文本输入框的回显模式
    def setUI(self):
        self.setWindowTitle('文本输入框的回显模式')
        formLayout = QFormLayout()

        normalLineEdit = QLineEdit()
        noEchoLineEdit = QLineEdit()
        passwordLineEdit = QLineEdit()
        passwordEchoOnEditLineEdit = QLineEdit()

        formLayout.addRow("Normal", normalLineEdit)
        formLayout.addRow("NoEcho", noEchoLineEdit)
        formLayout.addRow("Password", passwordLineEdit)
        formLayout.addRow("PasswordEchoOnEditLineEdit", passwordEchoOnEditLineEdit)
        normalLineEdit.setPlaceholderText("Normal")
        noEchoLineEdit.setPlaceholderText("NoEcho")
        passwordLineEdit.setPlaceholderText("Password")
        passwordEchoOnEditLineEdit.setPlaceholderText("PasswordEchoOnEdit")

        normalLineEdit.setEchoMode(QLineEdit.Normal)
        noEchoLineEdit.setEchoMode(QLineEdit.NoEcho)
        passwordLineEdit.setEchoMode(QLineEdit.Password)
        passwordEchoOnEditLineEdit.setEchoMode(QLineEdit.PasswordEchoOnEdit)

        self.setLayout(formLayout)





if __name__ == '__main__':
    app = QApplication(sys.argv)
    main = QlineEditEchoMode()
    main.show()
    sys.exit(app.exec_())