import logging

from connectors.csv_connector import CSVDataStore
from connectors.json_connector import JSONDataStore
from connectors.mongo_connector import MongoDataStore
from connectors.psg_connector import PSGDataStore


__author__ = "Andrew Gafiychuk"


class DataStore(object):
    """
    DataStore Fabric.
    
    Class DataStore what implement Class Fabrics for auto create, configure,
    and connect to different type of data store such as json file, csv file,
    PostgreSQL data base and Mongo data base.
    
    set_ds_type() - User can set type of DS.
    get_ds_list() - User can watch available DS.
    create_data_store() - Create and connect to DS.
    
    """
    _data_stores = {"csv": CSVDataStore, "json": JSONDataStore,
                    "postgre": PSGDataStore, "mongo":MongoDataStore}

    def __init__(self, ds_type=None):
        self.ds_type = ds_type

    def create_data_store(self):
        """
        Create and connect to established DS.
        
        """
        if not self.ds_type:
            print("[ERR:]Choice some DS Type.\n"
                  "Use get_ds_list()")

            return None

        if self.ds_type.lower() in self._data_stores.keys():
            datastore = self._data_stores[self.ds_type]

            logging.debug("[+]DS created - {0}"
                          .format(self.ds_type))

            # forget to pass db settings to db class init?
            return datastore()
        else:
            print("[ERR:]Unknown DS type.\n"
                  "Use get_ds_list() for watch accessible DS.")

            return None

    def get_ds_list(self):
        """
        Print available DS types.
        
        """
        ds_list = self._data_stores.keys()

        print("Available data stores:")
        for ds in ds_list:
            print("{0}".format(ds))

    def set_ds_type(self, ds_type):
        """
        Use this method to set/change DS type.
        
        """
        if not isinstance(ds_type, str):
            print("[+]DataStore type must be string!!!\n"
                  "Use .get_ds_list()")

        self.ds_type = ds_type
