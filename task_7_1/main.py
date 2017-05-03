import sys
import logging

from time import sleep
from _gui import Ui_MainWindow
from data_store import DataStore
from config import Configure
from PyQt5 import QtCore, QtWidgets
from scraper import Scraper


__author__ = "Andrew Gafiychuk"


class ScraperThread(QtCore.QThread):
    """
    Class implement Scrappint the overclockers.ua and
    fill the table by it data.
    Use QThread.
    
    """
    send_data = QtCore.pyqtSignal(object)
    t_finish = QtCore.pyqtSignal()

    def __init__(self, page_count):
        super(self.__class__, self).__init__()

        self.page_count = page_count

    def run(self):
        try:
            sc = Scraper(self.page_count)
            data = sc.start()

            self.send_data.emit(data)

        except Exception as err:
            print(err)

        finally:
            self.t_finish.emit()

    def __del__(self):
        self.wait()


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
        try:
            fact = DataStore()
            fact.set_ds_type(self.ds_type)

            ds = fact.create_data_store()

            ds.set_user(self.params["user"])
            ds.set_password(self.params["password"])
            ds.set_host(self.params["host"])
            ds.set_port(self.params["port"])
            ds.set_db(self.params["db_name"])
            ds.set_table(self.params["table"])

            ds.connect()

            data = ds.get_all_data()

            self.fill_table.emit(data)
            self.sleep(2)

        except Exception as err:
            print(err)

        finally:
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
        try:
            fact = DataStore()
            fact.set_ds_type(self.f_type)

            ds = fact.create_data_store()

            if self.f_type == "json" or self.f_type == "csv":
                ds.set_file(self.params[self.f_type])
            if self.f_type == "postgre" or self.f_type == "mongo":
                ds.set_user(self.params["user"])
                ds.set_password(self.params["password"])
                ds.set_host(self.params["host"])
                ds.set_port(self.params["port"])
                ds.set_db(self.params["db_name"])
                ds.set_table(self.params["table"])

            ds.connect()

            for row in self.data:
                ds.insert_unique(*row)

            self.sleep(2)

        except Exception as err:
            print(err)

        finally:
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

        self.btn_exp.clicked.connect(self.export)
        self.btn_fill.clicked.connect(self.fill)
        self.btn_save.clicked.connect(self.save)
        self.btn_scrapp.clicked.connect(self.scrap)

    def fill(self):
        """
        Press 'Fill' key to call this method.
        Load data from selected data store and btn_fill table by it.
        Use QThread
        
        """
        self.set_disable()

        store_type = self.cmb_exp.currentText()

        try:
            self.fill_thread = FillTableThread(
                store_type, self.config)
            self.fill_thread.fill_table.connect(
                self._fill_table)
            self.fill_thread.t_finish.connect(
                self.set_enable)
            self.fill_thread.start()

        except Exception as err:
            print("Fill method error...\n"
                  "{0}".format(err))

    def export(self):
        """
        Press 'Export to JSON' key to call this method.
        Method takes all loaded data? convert and save it to
        JSON file.
        Use QThread.
        
        """
        self.set_disable()

        f_type = self.cmb_save.currentText()

        if not self.data:
            print("[+]Not data to Export...")
            return
        try:
            self.exp_thread = ExportThread(
                self.data, f_type, self.config)
            self.exp_thread.t_finish.connect(
                self.set_enable)
            self.exp_thread.start()

        except Exception as err:
            print("Export error...\n"
                  "{0}".format(err))

    def save(self):
        """
        Method for saving Scrap results to DB.
        Works throw QThread.
        
        """
        self.set_disable()

        f_type = self.cmb_ds.currentText()

        if not self.data:
            print("[+]No data to Saving...")
            return

        try:
            self.exp_thread = ExportThread(
                self.data, f_type, self.config)
            self.exp_thread.t_finish.connect(
                self.set_enable)
            self.exp_thread.start()

        except Exception as err:
            print("Save data error...\n"
                  "{0}".format(err))

    def scrap(self):
        """
        Method start scrap.py script for scrap data from site.
        Takes data, parse, structer it and fill table.
        Use QThread.
        
        """
        self.set_disable()

        sleep(1)

        page_count = self.page_count_box.value()

        if page_count <= 0:
            page_count = 1

        try:
            self.scrap_thread = ScraperThread(page_count)
            self.scrap_thread.send_data.connect(
                self._fill_scrap_table)
            self.scrap_thread.t_finish.connect(
                self.set_enable)
            self.scrap_thread.start()

        except Exception as err:
            print("Scraper error...\n"
                  "{0}".format(err))

    def _fill_scrap_table(self, data):
        """
        Fill Table by Scraper result data.
        Tab Scraper.
        
        """
        self.data = data
        self.table_scrap.setRowCount(len(self.data))
        for num, row in enumerate(self.data):
            self.table_scrap.setItem(
                num, 0, QtWidgets.QTableWidgetItem(row[0]))
            self.table_scrap.setItem(
                num, 1, QtWidgets.QTableWidgetItem(row[1]))
            self.table_scrap.setItem(
                num, 2, QtWidgets.QTableWidgetItem(row[2]))
            self.table_scrap.setItem(
                num, 3, QtWidgets.QTableWidgetItem(row[3]))

    def _fill_table(self, data_list):
        """
        Fill table by data from DB.
        Tab Export.

        """
        self.data = data_list

        self.table_export.setRowCount(len(data_list))
        for num, row in enumerate(data_list):
            self.table_export.setItem(num, 0,
                               QtWidgets.QTableWidgetItem(row[0]))
            self.table_export.setItem(num, 1,
                               QtWidgets.QTableWidgetItem(row[1]))
            self.table_export.setItem(num, 2,
                               QtWidgets.QTableWidgetItem(row[2]))
            self.table_export.setItem(num, 3,
                               QtWidgets.QTableWidgetItem(row[3]))

    def set_enable(self):
        """
        Enable all elements by operations done.

        """
        self.btn_fill.setEnabled(True)
        self.btn_exp.setEnabled(True)
        self.btn_scrapp.setEnabled(True)
        self.btn_save.setEnabled(True)

        self.cmb_ds.setEnabled(True)
        self.cmb_exp.setEnabled(True)
        self.cmb_save.setEnabled(True)

        self.page_count_box.setEnabled(True)

    def set_disable(self):
        """
        Disable all elements while operations working.

        """
        self.btn_fill.setDisabled(True)
        self.btn_exp.setDisabled(True)
        self.btn_scrapp.setDisabled(True)
        self.btn_save.setDisabled(True)

        self.cmb_ds.setDisabled(True)
        self.cmb_exp.setDisabled(True)
        self.cmb_save.setDisabled(True)

        self.page_count_box.setDisabled(True)


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