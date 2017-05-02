# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.8.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):

    def setupUi(self, MainWindow):

        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(637, 584)

        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName("verticalLayout_2")

        self.main_tab = QtWidgets.QTabWidget(self.centralwidget)
        self.main_tab.setObjectName("main_tab")

        self.tab_scraper = QtWidgets.QWidget()
        self.tab_scraper.setObjectName("tab_scraper")

        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_scraper)
        self.verticalLayout.setObjectName("verticalLayout")

        self.table_scrap = QtWidgets.QTableWidget(self.tab_scraper)
        self.table_scrap.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.table_scrap.setObjectName("table_scrap")
        self.table_scrap.setColumnCount(4)
        self.table_scrap.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.table_scrap.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_scrap.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_scrap.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()

        self.table_scrap.setHorizontalHeaderItem(3, item)
        self.verticalLayout.addWidget(self.table_scrap)

        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")

        spacerItem = QtWidgets.QSpacerItem(40, 20,
                                QtWidgets.QSizePolicy.Expanding,
                                QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout.addItem(spacerItem)
        self.label = QtWidgets.QLabel(self.tab_scraper)
        self.label.setObjectName("label")

        self.horizontalLayout.addWidget(self.label)
        self.page_count_box = QtWidgets.QSpinBox(self.tab_scraper)
        self.page_count_box.setObjectName("page_count_box")

        self.horizontalLayout.addWidget(self.page_count_box)
        self.btn_scrapp = QtWidgets.QPushButton(self.tab_scraper)
        self.btn_scrapp.setObjectName("btn_scrapp")
        self.horizontalLayout.addWidget(self.btn_scrapp)

        self.cmb_ds = QtWidgets.QComboBox(self.tab_scraper)
        self.cmb_ds.setObjectName("cmb_ds")
        self.cmb_ds.addItem("")
        self.cmb_ds.addItem("")
        self.cmb_ds.addItem("")
        self.cmb_ds.addItem("")

        self.horizontalLayout.addWidget(self.cmb_ds)
        self.btn_save = QtWidgets.QPushButton(self.tab_scraper)
        self.btn_save.setObjectName("btn_save")

        self.horizontalLayout.addWidget(self.btn_save)
        self.verticalLayout.addLayout(self.horizontalLayout)

        self.main_tab.addTab(self.tab_scraper, "")

        self.tab_export = QtWidgets.QWidget()
        self.tab_export.setObjectName("tab_export")

        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.tab_export)
        self.verticalLayout_4.setObjectName("verticalLayout_4")

        self.table_export = QtWidgets.QTableWidget(self.tab_export)
        self.table_export.setObjectName("table_export")
        self.table_export.setColumnCount(4)
        self.table_export.setRowCount(0)

        item = QtWidgets.QTableWidgetItem()
        self.table_export.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_export.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.table_export.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()

        self.table_export.setHorizontalHeaderItem(3, item)

        self.verticalLayout_4.addWidget(self.table_export)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        spacerItem1 = QtWidgets.QSpacerItem(40, 20,
                        QtWidgets.QSizePolicy.Expanding,
                        QtWidgets.QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(spacerItem1)
        self.cmb_exp = QtWidgets.QComboBox(self.tab_export)
        self.cmb_exp.setObjectName("cmb_exp")
        self.cmb_exp.addItem("")
        self.cmb_exp.addItem("")

        self.horizontalLayout_2.addWidget(self.cmb_exp)
        self.btn_fill = QtWidgets.QPushButton(self.tab_export)
        self.btn_fill.setObjectName("btn_fill")

        self.horizontalLayout_2.addWidget(self.btn_fill)
        self.cmb_save = QtWidgets.QComboBox(self.tab_export)
        self.cmb_save.setObjectName("cmb_save")
        self.cmb_save.addItem("")
        self.cmb_save.addItem("")

        self.horizontalLayout_2.addWidget(self.cmb_save)
        self.btn_exp = QtWidgets.QPushButton(self.tab_export)
        self.btn_exp.setObjectName("btn_exp")

        self.horizontalLayout_2.addWidget(self.btn_exp)
        self.verticalLayout_4.addLayout(self.horizontalLayout_2)

        self.main_tab.addTab(self.tab_export, "")
        self.verticalLayout_2.addWidget(self.main_tab)

        MainWindow.setCentralWidget(self.centralwidget)

        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 637, 21))
        self.menubar.setObjectName("menubar")

        MainWindow.setMenuBar(self.menubar)

        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")

        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.main_tab.setCurrentIndex(0)

        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate

        MainWindow.setWindowTitle(_translate("MainWindow", "Scraper v1.1"))
        MainWindow.setWindowIcon(QtGui.QIcon("src\scraper_ico.png"))

        item = self.table_scrap.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Author"))
        item = self.table_scrap.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.table_scrap.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Link"))
        item = self.table_scrap.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Post"))

        self.label.setText(_translate("MainWindow", "Page count"))

        self.btn_scrapp.setText(_translate("MainWindow", "Scrapp..."))

        self.cmb_ds.setItemText(0, _translate("MainWindow", "postgre"))
        self.cmb_ds.setItemText(1, _translate("MainWindow", "mongo"))
        self.cmb_ds.setItemText(2, _translate("MainWindow", "json"))
        self.cmb_ds.setItemText(3, _translate("MainWindow", "csv"))

        self.btn_save.setText(_translate("MainWindow", "Save"))

        self.main_tab.setTabText(
            self.main_tab.indexOf(self.tab_scraper),
            _translate("MainWindow", "Scraper"))

        item = self.table_export.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Author"))
        item = self.table_export.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Title"))
        item = self.table_export.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Link"))
        item = self.table_export.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Post"))

        self.cmb_exp.setItemText(0, _translate("MainWindow", "postgre"))
        self.cmb_exp.setItemText(1, _translate("MainWindow", "mongo"))

        self.btn_fill.setText(_translate("MainWindow", "-> Fill"))

        self.cmb_save.setItemText(0, _translate("MainWindow", "json"))
        self.cmb_save.setItemText(1, _translate("MainWindow", "csv"))

        self.btn_exp.setText(_translate("MainWindow", "->Export..."))

        self.main_tab.setTabText(
            self.main_tab.indexOf(self.tab_export),
            _translate("MainWindow", "Export"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)

    MainWindow = QtWidgets.QMainWindow()

    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)

    MainWindow.show()

    sys.exit(app.exec_())
