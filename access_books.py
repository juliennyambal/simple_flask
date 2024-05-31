import requests
from json import dumps

url = "http://localhost:5000"
headers = {'Content-Type': 'application/json', 'charset': 'utf-8'}

get_all_books = "/books"

books = requests.get(url=f"{url}{get_all_books}", timeout=10)
print(books.json()['books'])

book_items = books.json()['books']

insert_books = ["pepsi", "7up", "8up", "9up", "miranda", "the great one"]
insert_description = ["great", "nice", "good", "marvelous", "amazing", "the great one"]

for book, description in zip(insert_books, insert_description):
    payload = {"name": book, "description": description}
    response = requests.post(url=f"{url}{get_all_books}", data=dumps(payload), headers=headers, timeout=10)
    print(response)

id = 1
book_id = requests.get(url=f"{url}/books/{id}", timeout=10)
print(book_id.json())