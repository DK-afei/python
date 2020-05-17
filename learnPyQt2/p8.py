from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5.QtCore import *
from learnPyQt2.third import *
import sys
#填充的数据1
# data = []
# data.append(('Popultating', 'QtableWidget'))
# data.append(('With data', 'In Python'))
# data.append(('Is easy', 'Job'))
#填充的数据2
data = ['PyQt5', 'Is', 'Awesome']

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.tableWidget.setRowCount(3)
        self.ui.tableWidget.setColumnCount(2)
        #点击行列标题来设置行列按升序或降序排序
        # self.ui.tableWidget.setSortingEnabled(True)
        self.ui.tableWidget.setHorizontalHeaderLabels(('Column 1', 'Column 2'))
        self.ui.tableWidget.setVerticalHeaderLabels(('row 1', 'row 2', 'row 3'))
        row=0
        #添加QComboBox
        for item in data:
            cellinfo=QTableWidgetItem(item)
            #添加组合框到table部件里
            # combo = QtWidgets.QComboBox()
            # combo.addItem("First item")
            # combo.addItem("Second item")
            #添加进度条progressbar到table部件里
            # progressbar = QtWidgets.QProgressBar()
            #添加点选框到table部件里
            checkbox = QtWidgets.QCheckBox()
            self.ui.tableWidget.setItem(row, 0, cellinfo)
            self.ui.tableWidget.setCellWidget(row, 1, checkbox)
            row += 1
        #数据填充1
        # for tup in data:
        #     col=0
        #     for item in tup:
        #         cellinfo=QTableWidgetItem(item)
        #         #设置表格只读，不可编辑
        #         cellinfo.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)
        #         self.ui.tableWidget.setItem(row, col, cellinfo)
        #         col+=1
        #     row+=1
        #默认升序排序
        # self.ui.tableWidget.sortItems(0)
        #设置列索引并按升序排序
        # self.ui.tableWidget.sortByColumn(0, QtCore.Qt.AscendingOrder)
        #降序排序
        # self.ui.tableWidget.sortItems(0, QtCore.Qt.DescendingOrder)

app = QtWidgets.QApplication([])
win = mywindow()
win.show()
sys.exit(app.exec())