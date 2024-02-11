class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return f" Title: {self.title}, Author: {self.author},Pages: {self.pages}"

    def __len__(self):
        return self.pages


if __name__ == "__main__":
    book1 = Book("Python Programming", "Ivan Ivanov", 330)
    book2 = Book("Introduction to Machine Learning", "Petar Petrov", 250)

    print("Book1:", book1)
    print("Book2:",book2)

    print("Number of pages in Book1:", len(book1))
    print("Number of pages in Book2:", len(book2))

