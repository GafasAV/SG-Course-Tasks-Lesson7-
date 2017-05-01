from connectors.json_connector import JSONDataStore

__author__ = "Andrew Gafiychuk"


if __name__ == '__main__':
    data_store = JSONDataStore()
    data_store.connect()

    data_list = data_store.get_all_data()
    for row in data_list:
        print(row)

    post_list = data_store.get_data_by_author("Janick")
    for row in post_list:
        print(">>>{0}".format(row))
