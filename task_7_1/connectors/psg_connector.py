import logging
import psycopg2

from connectors.connector_interface import AbsStoreConnector


__author__ = "Andrew Gafiychuk"


class PSGDataStore(AbsStoreConnector, object):
    """
    Class for create and connect to data base, for saving
    parsed data from overclockers.ua.
    Used PostgreSQL.
    Create table named overclockers.
    connect() - create DB connecting use(username, passwd, host, db_name, table_name)
    _create_table() - create overclockers table.
    insert_data() - takes 4 params and save it in DB.
    set_db() - Allow to change target DB in Postgre.
    set_table() - Allow to change target Table is PostgreSQL DB.
    
    """
    def __init__(self,
                 user="postgres", password="12345",
                 host="localhost", db_name="postgres",
                 table="overclockers"):
        """
        Init DB params for connecting.
        
        """
        self.user = user
        self.passwd = password
        self.host = host
        self.db_name = db_name
        self.table = table

        self.conn = None
        self.cursor = None

    def __del__(self):
        if self.cursor or self.conn:
            self.cursor.close()
            self.conn.close()

    def connect(self):
        """
        Create DB connecting uses _main params.
        return DB cursor as self.cursor
        
        """
        logging.debug("[+]DB Connecting...")

        try:
            print(self.db_name, self.user, self.passwd, self.host)
            self.conn = psycopg2.connect(database=self.db_name,
                                         user=self.user,
                                         password=self.passwd,
                                         host=self.host)

            self.cursor = self.conn.cursor()
            self._create_table()

            logging.debug("[+]DB Connected success !!!")

        except psycopg2.Error as db_err:
            logging.error("[+]DB Connecting problem...\n"
                          "{0}".format(db_err))

    def _create_table(self):
        """
        Create table in standart DB postgre.
        Table - overclockers.
        
        """
        try:
            self.cursor.execute(
                "CREATE TABLE IF NOT EXISTS {0}"
                "(id SERIAL PRIMARY KEY,"
                "author VARCHAR,"
                "title TEXT,"
                "link CHAR (300) UNIQUE,"
                "post TEXT);".format(self.table))

            self.conn.commit()

            logging.debug("[+]Table {0} created !!!"
                          .format(self.table))

        except psycopg2.Error as db_err:
            logging.debug("[+]Table creating error...\n"
                          "{0}".format(db_err))

    def insert_data(self, author, title, link, post):
        """
        Takes params and save it in DB.
        
        """
        try:
            self.cursor.execute(
                '''INSERT INTO {0} (author, title, link, post)
                 VALUES (%s, %s, %s, %s);'''.format(self.table),
                (author, title, link, post))

            self.conn.commit()

            logging.info("Data saved...")

        except psycopg2.Error as db_err:
            logging.error("[+]Data save error...\n"
                          "[+]DB\Connecting problem..."
                          "{0}".format(db_err))

    def get_all_data(self):
        """
        Loads data from DB and return it.
        
        """
        try:
            self.cursor.execute("SELECT * FROM {0};"
                                .format(self.table))
            data = self.cursor.fetchall()

            result_list = self.filter_data(data)

            return result_list

        except psycopg2.Error as db_err:
            logging.error("[+]Get data error...\n"
                          "{0}".format(db_err))

    def get_data_by_author(self, author):
        """
        Load all post for input author.
        
        """
        try:
            self.cursor.execute(
                "SELECT * FROM {0} WHERE author = %s;"
                .format(self.table), (author, ))

            data = self.cursor.fetchall()

            result_list = self.filter_data(data)

            return result_list

        except psycopg2.Error as db_err:
            logging.error("[+]Get data error...\n"
                          "{0}".format(db_err))
                          
    def insert_unique(self, author, title, link, post):
        """
        Insert data into DB without duplicate.
        Check by link.
        
        """
        try:
            self.cursor.execute(
                '''INSERT INTO {0} (author, title, link, post)
                   VALUES (%s, %s, %s, %s)
                   ON CONFLICT (link)
                   DO NOTHING;'''
                .format(self.table), (author, title, link, post))

            self.conn.commit()

            logging.info("[+]Data saved or already exists !")

        except psycopg2.Error as db_err:
            logging.error("[+]Data insert error...\n"
                          "{0}".format(db_err.pgerror))
            logging.error(db_err.diag.message_primary)

    def set_db(self, name):
        """
        Use this method to change target PostgreDB.
        
        """
        if not isinstance(name, str):
            raise TypeError("[+]Name must be a string!!!")
        else:
            self.db_name = name

    def set_table(self, name):
        """
        Use this method for change target Table in PostgreDB.
         
        """
        if not isinstance(name, str):
            raise TypeError("[+]Name must be a string!!!")
        else:
            self.table = name

    def filter_data(self, data):
        clear_list = []

        for record in data:
            clear_list.append((*record[1:],))

        return clear_list
