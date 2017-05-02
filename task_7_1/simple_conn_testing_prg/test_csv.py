from connectors.csv_connector import CSVDataStore


__author__ = "Andrew Gafas"


if __name__ == '__main__':
    datastore = CSVDataStore()
    datastore.connect()

    data = ("TestUser","TitleTestUser",
            "http://google3000.com","some test text",)

    datastore.insert_unique(*data)

    result_list = datastore.get_all_data()
    for row in result_list:
        print(row)

    print(">>>")
    result_list = datastore.get_data_by_author('Petro')
    for record in result_list:
        print(record)
