import logging
import pymongo

from connectors.connector_interface import AbsStoreConnector


__author__ = "Andrew Gafiychuk"


class MongoDataStore(AbsStoreConnector, object):
    """
    Class for create and connect to data base, for saving
    parsed data from overclockers.ua.
    Used MongoDB.
    Create db and collection named overclockers.
    
    connect() - create DB connecting use(host, db_name, table_name)
    _create_collection() - create overclockers collection.
                           Set an unique index by <link> row. 
    insert_unique() - takes 4 params and save it in DB. 
                      Check <link> too unique.
    get_all_data() - Select ALL docs from collection.
    get_data_by_author() - Selects all documents 
                        for one specified author.
    set_db() - Allows to change target DB.
    set_table() - Allows to change target DB Table.
    
    """
    def __init__(self, user="mongo", password="12345",
                 host="localhost", port="27017",
                 db_name="overclockers", table="overclockers"):
        """
        Init all params for connecting to MongoDB.

        """
        self.user = user
        self.passwd = password

        self.host = host
        self.port = port

        self.db_name = db_name
        self.collection_name = table

        self.client = None
        self.db = None
        self.coll = None

    def __del__(self):
        """
        Check if connecting steel alive and close them if.
        
        """
        if self.client:
            self.client.close()

    def connect(self):
        """
        Connect to DB.
        
        """
        try:
            self.client = pymongo.MongoClient(
                host=self.host, port=int(self.port))

            self._create_collection()
            logging.debug("[+]MongoDB connected!!!")

        except:
            logging.error("[+]MongoDB connecting problem...")

    def _create_collection(self):
        """
        Create collection for specified DB.
        Set link-row to unique index.
        
        """
        self.db = self.client[self.db_name]
        #self.db.authenticate(self.user, self.passwd)
        
        self.coll = self.db[self.collection_name]

        # Unique record post by hiper-link
        self.coll.create_index([("link", pymongo.ASCENDING)],
                               unique=True)

    def insert_unique(self, author, title, link, post):
        """
        Insert data into collection without duplicate.
        Checked by link.
        
        """
        doc = {"author": author, "title": title,
               "link": link, "post": post}

        try:
            result = self.coll.insert_one(doc)

            logging.info(">>>Data inserting success !!! ID {0}"
                         .format(result.inserted_id))

        except:
            logging.error("[+]Data insert error...\n")

    def get_all_data(self):
        """
        Loads ALL docs from coll. and return it.
 
        """
        try:
            cursor = self.coll.find({})
            result = []

            for record in cursor:
                result.append((*record.values(),)[1:5])

            return result
        except:
            logging.error("[+]Get data error...\n")

    def get_data_by_author(self, author):
        """
        Load all docs for specified author.

        """
        try:
            cursor = self.coll.find({"author": author})
            result = []

            for record in cursor:
                result.append((*record.values(),)[1:5])

            return result
        except:
            logging.error("[+]Get data error...\n")

    def set_user(self, user_name):
        """
        Setting User name DB param.
        
        """
        if not isinstance(user_name, str):
            raise TypeError("[+]User name must be string!!!")
        else:
            self.user = user_name

    def set_password(self, password):
        """
        Setting the DB password param.
        
        """
        if not isinstance(password, str):
            raise TypeError("[+]Set DB password as string!!!")
        else:
            self.passwd = password

    def set_host(self, host):
        """
        Setting the host addr for DB.
        
        """
        if not isinstance(host, str):
            raise TypeError("[+]Set Host name as string!!!")
        else:
            self.host = host

    def set_port(self, port):
        """
        Setting DB connection port param.
         
        """
        self.port = port

    def set_db(self, db_name):
        """
        Use this method to change DB name for data storing.
        
        """
        if not isinstance(db_name, str):
            raise TypeError("[+]Name must be a string!!!")
        else:
            self.db_name = db_name

    def set_table(self, table_name):
        """
        Use this method to change COLLECTION for data CRUD.

        """
        if not isinstance(table_name, str):
            raise TypeError("[+]Name must be a string!!!")
        else:
            self.collection_name = table_name
