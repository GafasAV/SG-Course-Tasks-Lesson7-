import json
import logging

from connectors.connector_interface import AbsStoreConnector

__author__ = "Andrew Gafiychuk"


class JSONDataStore(AbsStoreConnector, object):
    """
    Class implement connector interface for create/connect/use json file
    as data store for CRUD data from scrapper. Scrapp overclockers.ua.
    
    connect() - Private method for check/create/connect for json file.
    insert_unique() - Takes data, check it, and save to json file as unique.
    get_all_data() - Read all data from json file and return it as list.
    get_data_by_author() - Read data from json file, filtering by author name.
                        return all post for specified author.
    set_file() - Allowed to change target file for working.
    _check_link() - check for duplication post by target link.
    
    """
    def __init__(self, json="overclockers.json"):
        """
        Constructor.
        Init _main params for connection to file.

        """
        self.filename = json
        self.file = None

    def __del__(self):
        if self.file:
            self.file.close()

    def connect(self):
        """
        Private method for creating and opening target json file for
        data CRUD.
        
        """
        if not isinstance(self.filename, str):
            raise TypeError("[+]File name must be string!!!")

        try:
            self.file = open(
                self.filename, "a+", encoding="utf-8", newline="")
            logging.info("[+]File {0} created success!!!"
                         .format(self.filename))

        except OSError:
            logging.error("[+]File {0} IO error..."
                          .format(self.filename))

    def insert_unique(self, author, title, link, post):
        """
        Takes params tuple, create an json object and save to json file.
        Save unique data by post link.

        """
        if self._check_link(link):
            logging.info("[+]This post alredy exist!!!")

            return
        else:
            data = json.dumps({'author': author, 'title': title,
                               'link': link, 'post': post})

            try:
                self.file.write(data + "\n")

                logging.info("[+]Data saved success!!!")

            except:
                raise IOError("[+]Data save error...")

    def get_all_data(self):
        """
        Return all existing records from file by rows.
         
        """
        self.file.seek(0)
        data_list = []

        try:
            for line in self.file:
                if not line:
                    break

                data = json.loads(line)
                data_list.append((*data.values(),))

            return data_list

        except:
            raise IOError("[+]File {0} read error..."
                          .format(self.filename))

    def get_data_by_author(self, author):
        """
        Method return all post for specified author name.        

        """
        if not isinstance(author, str):
            raise TypeError("[+]Author must be string!!!")

        self.file.seek(0)
        post_list = []

        try:
            for line in self.file:
                if not line:
                    break

                data = json.loads(line)

                if data['author'] == author:
                    post_list.append((*data.values(),))
                else:
                    continue

            return post_list

        except:
            raise IOError("[+]File {0} read error..."
                          .format(self.filename))

    def _check_link(self, link):
        """
        Private method for compare link for unique.
        This method helps for save only unique data by link.

        """
        self.file.seek(0)

        for line in self.file:
            if not line:
                break

            data = json.loads(line)
            if data["link"] == link:
                return True
            else:
                continue

        return False

    def set_file(self, name):
        """
        Use this method for change target json file.
 
        """
        if not isinstance(name, str):
            raise TypeError("[+]Name must be a string!!!")
        else:
            self.filename = name