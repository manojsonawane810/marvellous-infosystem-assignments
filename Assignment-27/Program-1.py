class BookStore:
    noOfBooks = 0

    def __init__(self, bookName, authorName):
        self.name = bookName
        self.author = authorName
        BookStore.noOfBooks = BookStore.noOfBooks + 1


    def display(self):
        print(f"{self.name} by {self.author}. No of books: {BookStore.noOfBooks}")

bObj1 = BookStore("Linux System Programming", "Robert Love")
bObj1.display()

bObj2 = BookStore("C Programming", "Dennis Ritchei")
bObj2.display()
