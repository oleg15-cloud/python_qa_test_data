import json
import csv

with open('../files/users.json', 'r') as users_file_json:
    users_json = json.load(users_file_json)
    result_users = []
    for user in users_json:
        result_users.append(
            {
                "name": user["name"],
                "gender": user["gender"],
                "address": user["address"],
                "age": user["age"],
                "books": []
            }
        )

with open("../files/book.csv", "r") as books_file_csv:
    books_json = csv.DictReader(books_file_csv)
    result_books = []
    for book in books_json:
        result_books.append(
            {
                "title": book["Title"],
                "author": book["Author"],
                "pages": book["Pages"],
                "genre": book["Genre"]
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
    json_dumps = json.dumps(add_books(users=result_users, books=result_books), indent=4)
    result.write(json_dumps)
