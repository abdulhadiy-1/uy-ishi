class Book:
    def __init__(self, id, name, author, count, price):
        self.id = id
        self.name = name
        self.author = author
        self.count = count
        self.price = price

    def __str__(self):
        return f"ID: {self.id}, Name: {self.name}, Author: {self.author}, Count: {self.count}, Price: {self.price}"

def file_w(books, filename):
    with open(filename, 'w') as file:
        for book in books:
            file.write(f"{book.id},{book.name},{book.author},{book.count},{book.price}\n")

def file_r(filename):
    books = []
    with open(filename, 'r') as file:
        lines = file.readlines()
        for line in lines:
            id, name, author, count, price = line.strip().split(',')
            books.append(Book(id, name, author, int(count), float(price)))
    return books

def count_id(books, id):
    for book in books:
        if book.id == id:
            if book.count > 0:
                book.count -= 1
                print(f"{book.name}: {book.count} ta coldi")
            else:
                print(f"{book.name} colmadi")
            return
    print(f"{id} id topilmadi")

def delete_id(books, id):
    for book in books:
        if book.id == id:
            books.remove(book)
            print(f"{id} id degi book ochti")
            return
    print(f"{id} id topilmadi")

books = [
    Book("1", "Book A", "Avtor A", 5, 2000),
    Book("2", "Book B", "Avtor B", 3, 1500),
    Book("3", "Book C", "Avtor C", 1, 2500)
]

file_w(books, "books.txt")

file_read = file_r("books.txt")


count_id(file_read, "1")

delete_id(file_read, "2")

for book in file_read:
    print(book)
