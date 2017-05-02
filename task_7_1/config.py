import json

from patterns.singletone import Singleton


__author__ = "Andrew Gafiychuk"


class Configure(Singleton, object):
    """
    Class used for configure some Scraper params, such as:
    files name, DB-name, table name, user login, password login, etc.
    
    You can use you own config file.
    Create it and set as cfg_file_name param.
    
    """
    def __init__(self, file ="config.cfg"):
        self.filename= file
        self.params = None

        self._config_read()

        # Testing param - remove later (Singleton pattern)
        self._singleton_mark = "EXAMPLE=1"

    def _config_read(self):
        try:
            file = open(self.filename, "r", encoding="utf-8")
            self.params = json.loads(file.read())

        except OSError:
            print("[+]Configure File read error...\n"
                  "{0}".format(self.filename))

    def show_config(self):
        for key, val in self.params.items():
            print("Param {0}: {1}".format(key, val))

    def getConfiguration(self):
        return self.params

    def get_username(self):
        return self.params["user"]

    def get_password(self):
        return self.params["password"]

    def get_host(self):
        return self.params["host"]

    def get_port(self):
        return self.params["port"]

    def get_dbname(self):
        return self.params["db_name"]

    def get_tablename(self):
        return self.params["table_name"]

    def get_json(self):
        return self.params["json"]

    def get_csv(self):
        return self.params["csv"]
