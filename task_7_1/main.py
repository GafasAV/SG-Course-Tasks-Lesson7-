import sys
import logging

from _gui import Ui_MainWindow
from data_store import DataStore
from PyQt5 import QtWidgets, QtCore
from config import Configure


__author__ = "Andrew Gafiychuk"


class FillTableThread(QtCore.QThread):
    """
    Class that implement DS reading throw the QThread.
    Takes DS type as param, load data from, and callback
    table btn_fill method.
    
    """
    fill_table = QtCore.pyqtSignal(list)
    t_finish = QtCore.pyqtSignal()

    def __init__(self, ds_type, config):
        super(self.__class__, self).__init__()
        self.ds_type = ds_type
        self.params = config.getConfiguration()

    def run(self):
        fact = DataStore()
        fact.set_ds_type(self.ds_type)

        ds = fact.create_data_store()
        ds.set_table(self.params["table"])
        ds.connect()

        data = ds.get_all_data()

        self.fill_table.emit(data)
        self.sleep(2)
        self.t_finish.emit()

    def __del__(self):
        self.wait()


class ExportThread(QtCore.QThread):
    """
    Class that implement data converting to JSON or CSV 
    and save it to file.
    Use QThread !!!
    
    """
    t_finish = QtCore.pyqtSignal()

    def __init__(self, data, f_type, config):
        super(self.__class__, self).__init__()

        self.f_type = f_type
        self.params = config.getConfiguration()
        self.data = data

    def run(self):
        fact = DataStore()
        fact.set_ds_type(self.f_type)

        ds = fact.create_data_store()
        ds.set_file(self.params[self.f_type])
        ds.connect()

        for row in self.data:
            ds.insert_unique(*row)

        self.sleep(2)
        self.t_finish.emit()

    def __del__(self):
        self.wait()


class MainForm(QtWidgets.QMainWindow, Ui_MainWindow):
    """
    Class that implementing software logic
    through the user interface form elements.
    
    """
    def __init__(self, config=None):
        super(self.__class__, self).__init__()
        self.config = config

        self.setupUi(self)

        self.btn_export.clicked.connect(self.export)
        self.btn_fill.clicked.connect(self.fill)

    def fill(self):
        """
        Press 'Fill' key to call this method.
        Load data from selected data store and btn_fill table by it.
         
        """
        store_type = self.cmb1.currentText()

        self.set_disable()

        self.fill_thread = FillTableThread(store_type, self.config)
        self.fill_thread.fill_table.connect(self._fill_table)
        self.fill_thread.t_finish.connect(self.set_enable)
        self.fill_thread.start()

    def export(self):
        """
        Press 'Export to JSON' key to call this method.
        Method takes all loaded data? convert and save it to
        JSON file.
        
        """
        format_type = self.cmb2.currentText()

        self.set_disable()

        if not self.data:
            print("[+]Not data to JSON Export")

        self.exp_thread = ExportThread(self.data, format_type, self.config)
        self.exp_thread.t_finish.connect(self.set_enable)
        self.exp_thread.start()

    def _fill_table(self, data_list):
        """
        Private method to load data 
        throw thread,used QThread class.
         
        """
        self.data = data_list

        self.table.setRowCount(len(self.data))
        for num, row in enumerate(self.data):
            self.table.setItem(num, 0,
                               QtWidgets.QTableWidgetItem(row[0]))
            self.table.setItem(num, 1,
                               QtWidgets.QTableWidgetItem(row[1]))
            self.table.setItem(num, 2,
                               QtWidgets.QTableWidgetItem(row[2]))
            self.table.setItem(num, 3,
                               QtWidgets.QTableWidgetItem(row[3]))

    def set_enable(self):
        """
        Enable all elements by operations done.
        
        """
        self.btn_fill.setEnabled(True)
        self.btn_export.setEnabled(True)
        self.cmb1.setEnabled(True)
        self.cmb2.setEnabled(True)

    def set_disable(self):
        """
        Disable all elements while operations working.
        
        """
        self.btn_fill.setDisabled(True)
        self.btn_export.setDisabled(True)
        self.cmb1.setDisabled(True)
        self.cmb2.setDisabled(True)


if __name__ == '__main__':
    logging.basicConfig(level=logging.DEBUG)
    logging.debug("[+]App started...")

    # Configure main program params...
    cfg = Configure()

    app = QtWidgets.QApplication(sys.argv)

    form = MainForm(config=cfg)
    form.show()

    logging.debug("[+]App set_enable...")
    sys.exit(app.exec_())