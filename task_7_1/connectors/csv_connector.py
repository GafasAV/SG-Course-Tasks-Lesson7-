import csv
import logging

from connectors.connector_interface import AbsStoreConnector


__author__ = "Andrew Gafiychuk"


class CSVDataStore(AbsStoreConnector, object):
    """
    Class for create and connect to csv-file, for saving
    parsed data from overclockers.ua.
    Used CSV-File.
    Create file named overclockers.csv.
    
    connect() - create file if not exist.
    insert_unique() - takes 4 params and save it in file. 
                      Check <link> too unique.
    _check_link() - check incoming link to unique.
    get_all_data() - Select ALL posts from file.
    get_data_by_author() - Selects all posts for one specified author.
    set_file() - Allow to change target csv file.
    
    """
    def __init__(self, csv="overclockers.csv"):
        """
        Init _main params for create .csv file.
        
        """
        self.filename = csv
        self.file = None

    def __del__(self):
        """
        Check file for opening and close him.
         
        """
        if self.file:
            self.file.close()

    def connect(self):
        """
        Check, create and open a .csv file.
         
        """
        if not isinstance(self.filename, str):
            raise TypeError("[+]File name must be string...")

        try:
            self.file = open(
                self.filename, "a+", encoding="utf-8", newline="")
            logging.info("[+]File {0} created success!!!"
                         .format(self.filename))

        except OSError:
            logging.error("[+]File {0} open error..."
                          .format(self.filename))

    def insert_unique(self, author, title, link, post):
        """
        Insert data in file without duplicate.
        Checked by link.
         
        """
        if self._check_link(link):
            logging.info(">>>This POST already exist!!!")

            return
        else:
            try:
                csv_writer = csv.writer(self.file, delimiter=';')

                csv_writer.writerow((author, title, link, post,))
                logging.info("[+]Data saved success!!!")

            except:
                raise IOError("[+]File {0} write error..."
                              .format(self.filename))

    def get_all_data(self):
        """
        Loads ALL posts from file and return it.
         
        """
        self.file.seek(0)
        result_list = []

        try:
            csv_reader = csv.reader(self.file, delimiter=';')

            for row in csv_reader:
                result_list.append((*row,))

            return result_list

        except:
            raise IOError("[+]File {0} read error..."
                          .format(self.filename))

    def get_data_by_author(self, author):
        """
        Load all posts for specified author.        
 
        """
        self.file.seek(0)
        auth_posts = []

        try:
            data = csv.reader(self.file, delimiter=';')

            for row in data:
                if row[0] == author:
                    auth_posts.append((*row,))
                else:
                    continue

            if len(auth_posts) == 0:
                logging.info("No Match !!!")

            return auth_posts

        except:
            raise IOError("[+]File {0} read error..."
                          .format(self.filename))

    def _check_link(self, link):
        """
        Additional method to check link for unique.
        
        """
        self.file.seek(0)
        data = csv.reader(self.file, delimiter=';')

        for row in data:
            if row[2] == link:
                return True
            else:
                continue

        return False

    def set_file(self, filename):
        """
        Use this method for change target csv-file.

        """
        if not isinstance(filename, str):
            raise TypeError("[+]File name must be string!!!")
        else:
            self.filename = filename
