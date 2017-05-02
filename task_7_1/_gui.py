# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(613, 551)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.table = QtWidgets.QTableWidget(self.centralwidget)
        self.table.setObjectName("table")
        self.table.setColumnCount(4)
        self.table.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()

        self.table.setHorizontalHeaderItem(3, item)
        self.verticalLayout_2.addWidget(self.table)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        self.cmb1 = QtWidgets.QComboBox(self.centralwidget)
        self.cmb1.setObjectName("cmb1")
        self.cmb1.addItem("")
        self.cmb1.addItem("")

        self.horizontalLayout.addWidget(self.cmb1)
        self.btn_fill = QtWidgets.QPushButton(self.centralwidget)
        self.btn_fill.setObjectName("btn_fill")

        self.horizontalLayout.addWidget(self.btn_fill)
        self.cmb2 = QtWidgets.QComboBox(self.centralwidget)
        self.cmb2.setObjectName("cmb2")
        self.cmb2.addItem("")
        self.cmb2.addItem("")

        self.horizontalLayout.addWidget(self.cmb2)
        self.btn_export = QtWidgets.QPushButton(self.centralwidget)
        self.btn_export.setObjectName("btn_export")

        self.horizontalLayout.addWidget(self.btn_export)
        self.verticalLayout_2.addLayout(self.horizontalLayout)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 613, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Scraper DS reader v1.0"))

        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Author"))
        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Link"))
        item = self.table.horizontalHeaderItem(3)

        item.setText(_translate("MainWindow", "Post"))
        self.cmb1.setItemText(0, _translate("MainWindow", "mongo"))
        self.cmb1.setItemText(1, _translate("MainWindow", "postgre"))

        self.btn_fill.setText(_translate("MainWindow", "-> Fill"))
        self.cmb2.setItemText(0, _translate("MainWindow", "csv"))
        self.cmb2.setItemText(1, _translate("MainWindow", "json"))

        self.btn_export.setText(_translate("MainWindow", "Export to JSON"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()

    sys.exit(app.exec_())

