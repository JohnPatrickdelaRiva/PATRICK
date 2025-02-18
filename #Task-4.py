class Book:
    def __init__(self, title, author, year_published):
        self.title = title
        self.author = author
        self.year_published = year_published
    def describe(self):
        print(f"Book Details:\nTitle: {self.title}\nAuthor: {self.author}\nYear Published: {self.year_published}")

book1 = Book("DON QUIXOTE", "MIGUEL DE CERVANTES", 2018)
book2 = Book("HARRY POTTER", "J.K. ROWLING", 1997)
book3 = Book("GREAT EXPECTATIONS", "CHARLES DICKENS", 1992)

book1.describe()
print() 
book2.describe()
print() 
book3.describe()