# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!
import sys

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):

    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(593, 505)

        self.gridLayout = QtWidgets.QGridLayout(Form)
        self.gridLayout.setObjectName("gridLayout")

        self.table = QtWidgets.QTableWidget(Form)
        self.table.setObjectName("tableWidget")
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

        self.gridLayout.addWidget(self.table, 0, 0, 1, 3)
        self.cmb = QtWidgets.QComboBox(Form)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.cmb.sizePolicy().hasHeightForWidth())

        self.cmb.setSizePolicy(sizePolicy)
        self.cmb.setObjectName("comboBox")
        self.cmb.addItem("")
        self.cmb.addItem("")

        self.gridLayout.addWidget(self.cmb, 1, 0, 1, 1)
        self.btn_fill = QtWidgets.QPushButton(Form)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_fill.sizePolicy().hasHeightForWidth())

        self.btn_fill.setSizePolicy(sizePolicy)
        self.btn_fill.setObjectName("pushButton_2")

        self.gridLayout.addWidget(self.btn_fill, 1, 1, 1, 1)
        self.btn_export = QtWidgets.QPushButton(Form)

        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Maximum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btn_export.sizePolicy().hasHeightForWidth())

        self.btn_export.setSizePolicy(sizePolicy)
        self.btn_export.setObjectName("pushButton")

        self.gridLayout.addWidget(self.btn_export, 1, 2, 1, 1)

        self.btn_export.raise_()
        self.btn_fill.raise_()

        self.table.raise_()
        self.cmb.raise_()

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate

        Form.setWindowTitle(_translate("Form", "Scraper v1.0"))
        Form.setWindowIcon(QtGui.QIcon("src\scraper_ico.png"))

        item = self.table.horizontalHeaderItem(0)
        item.setText(_translate("Form", "Author"))

        item = self.table.horizontalHeaderItem(1)
        item.setText(_translate("Form", "Title"))

        item = self.table.horizontalHeaderItem(2)
        item.setText(_translate("Form", "Link"))

        item = self.table.horizontalHeaderItem(3)
        item.setText(_translate("Form", "Post"))

        self.cmb.setItemText(0, _translate("Form", "mongo"))
        self.cmb.setItemText(1, _translate("Form", "postgre"))

        self.btn_fill.setText(_translate("Form", "-> Fill"))
        self.btn_export.setText(_translate("Form", "Export to JSON"))


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)

    Form = QtWidgets.QWidget()

    ui = Ui_Form()
    ui.setupUi(Form)

    Form.show()

    sys.exit(app.exec_())
