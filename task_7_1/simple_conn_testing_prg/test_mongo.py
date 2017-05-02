from connectors.mongo_connector import MongoDataStore


__author__ = "Andrew Gafiychuk"


if __name__ == '__main__':
    db = MongoDataStore(db_name="test", table="test")
    db.connect()

    record = ("SomeAuthor", "SomeAuthor Title", "http://google2000.com/search", "....Some Data....")

    db.insert_unique(*record)

    res_list = db.get_all_data()

    for record in res_list:
        print("User: {0}\n"
              "Title: {1}\n"
              "Link: {2}\n"
              "Post: {3}\n"
              .format(*record))

    res_list = db.get_data_by_author("SomeAuthor")

    for record in res_list:
        print(*record)
