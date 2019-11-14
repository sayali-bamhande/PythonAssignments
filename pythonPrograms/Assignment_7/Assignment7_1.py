class BookStore:
    NoOfBooks = 0

    def __init__(self, name, author):
        self.bookName = name
        self.bookAuthor = author
        BookStore.NoOfBooks = BookStore.NoOfBooks + 1

    def Display(self):
        print(self.bookName, "by", self.bookAuthor, end=". ")
        print("No of books :", self.NoOfBooks)


def main():
    Obj1 = BookStore("Linux System Programming", "Robert Love")
    Obj1.Display()

    Obj2 = BookStore("C Programming", "Dennis Ritchie")
    Obj2.Display()


if __name__ == "__main__":
    main()
