# -*- coding: utf-8 -*-
from PyQt4 import QtGui, QtCore
 
class MainWindow(QtGui.QWidget):
    def __init__(self, parent=None):
        QtGui.QMainWindow.__init__(self, parent)
 
        # 创建table和model
        table = QtGui.QTableView(parent=self)
        self.model = QtGui.QStandardItemModel(parent=self)
        self.model.setHorizontalHeaderLabels((u'姓名', u'年龄'))
        table.setModel(self.model)
 
        # 创建添加按钮
        button = QtGui.QPushButton(u'添加', parent=self)
 
        # 添加信号槽
        button.clicked.connect(self.add)
 
        # 创建一个垂直布局，用于防止表格和按钮
        layout = QtGui.QVBoxLayout()
        layout.addWidget(table)
        layout.addWidget(button)
 
        self.setLayout(layout)
 
    def add(self):
        dialog = Dialog(parent=self)
        if dialog.exec_():
            self.model.appendRow((
                QtGui.QStandardItem(dialog.name()),
                QtGui.QStandardItem(str(dialog.age())),
            ))
 
        dialog.destroy()
 
 
class Dialog(QtGui.QDialog):
    def __init__(self, parent=None):
        QtGui.QDialog.__init__(self, parent)
        self.resize(240, 200)
 
        # 表格布局，用来布局QLabel和QLineEdit及QSpinBox
        grid = QtGui.QGridLayout()
 
        grid.addWidget(QtGui.QLabel(u'姓名', parent=self), 0, 0, 1, 1)
 
        self.leName = QtGui.QLineEdit(parent=self)
        grid.addWidget(self.leName, 0, 1, 1, 1)
 
        grid.addWidget(QtGui.QLabel(u'年龄', parent=self), 1, 0, 1, 1)
 
        self.sbAge = QtGui.QSpinBox(parent=self)
        grid.addWidget(self.sbAge, 1, 1, 1, 1)
 
        # 创建ButtonBox，用户确定和取消
        buttonBox = QtGui.QDialogButtonBox(parent=self)
        buttonBox.setOrientation(QtCore.Qt.Horizontal) # 设置为水平方向
        buttonBox.setStandardButtons(QtGui.QDialogButtonBox.Cancel|QtGui.QDialogButtonBox.Ok) # 确定和取消两个按钮
        # 连接信号和槽
        buttonBox.accepted.connect(self.accept) # 确定
        buttonBox.rejected.connect(self.reject) # 取消
 
        # 垂直布局，布局表格及按钮
        layout = QtGui.QVBoxLayout()
 
        # 加入前面创建的表格布局
        layout.addLayout(grid)
 
        # 放一个间隔对象美化布局
        spacerItem = QtGui.QSpacerItem(20, 48, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        layout.addItem(spacerItem)
 
        # ButtonBox
        layout.addWidget(buttonBox)
 
        self.setLayout(layout)
 
    def name(self):
        return self.leName.text()
 
    def age(self):
        return self.sbAge.value()
 
 
if __name__ == '__main__':
    import sys
    app = QtGui.QApplication(sys.argv)
    mainWindow = MainWindow()
    mainWindow.show()
    sys.exit(app.exec_())