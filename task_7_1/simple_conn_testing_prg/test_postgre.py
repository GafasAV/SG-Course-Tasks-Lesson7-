from connectors.psg_connector import PSGDataStore


__author__ = "Andrew Gafiychuk"


if __name__ == '__main__':
    db = PSGDataStore()
    db.connect()

    data = db.get_all_data()

    for num, record in enumerate(data):
        print(">>>" + str(num))
        print("Author: {0}\n"
              "Title: {1}\n"
              "Link: {2}\n"
              "Post\n{3}"
              .format(record[1], record[2], record[3], record[4]))
        print("[+]" * 120)

    name = input("Input author name: ")
    posts = db.get_data_by_author(name)

    for post in posts:
        print(post)
