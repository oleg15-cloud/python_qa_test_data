import json
import csv

with open('../files/users.json', 'r') as users_file_json:
    users_json = json.load(users_file_json)
    result_users = []
    for item in users_json:
        result_users.append(
            {
                "name": item["name"],
                "gender": item["gender"],
                "address": item["address"],
                "age": item["age"],
                "books": []
            }
        )

with open("../files/book.csv", "r") as books_file_csv:
    reader = csv.DictReader(books_file_csv)
    result_books = []
    for item in reader:
        result_books.append(
            {
                "title": item["Title"],
                "author": item["Author"],
                "pages": item["Pages"],
                "genre": item["Genre"]
            }
        )


def add_books(users, books):
    user_index = 0
    while len(books) != 0:
        if user_index == len(users):
            user_index = 0
            users[user_index]["books"].append(books.pop(0))
            user_index += 1
        else:
            users[user_index]["books"].append(books.pop(0))
            user_index += 1
    return users


with open('../files/result.json', 'w') as result:
    json_dump = json.dumps(add_books(users=result_users, books=result_books), indent=4)
    result.write(json_dump)
