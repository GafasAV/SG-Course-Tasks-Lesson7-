from abc import ABC


__author__ = "Andrew Gafiychuk"


class AbsStoreConnector(ABC):
    """
    Implement simple interface with _main methods 
    for CRUD operation with different data-store
    (DB, csv-file, json-file, etc).
    
    You can add you own DataStore inheriting this 
    interface, and add class to fabric uses special
    methods.
    
    Show docs!!!
    
    """
    def connect(self):
        """
        To create connecting for each data-store type.
        
        """
        raise NotImplemented

    def insert_unique(self, author, title, link, post):
        """
        Override method to add data by one unique params.
        
        """
        raise NotImplemented

    def get_all_data(self):
        """
        Method that take all data from data store and ret it.
        
        """
        raise NotImplemented

    def get_data_by_author(self, author):
        """
        Get data that belongs one author and ret it.
        
        """
        raise NotImplemented
