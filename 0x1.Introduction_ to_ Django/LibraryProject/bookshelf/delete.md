# Delete retrieved books

In [15]: retrieved_book.delete()

In [17]: book = Book.objects.all()

In [18]: print(book)
#Expected output

<QuerySet [<Book: Book: self.title, self.author, self.publication_year>, <Book: Book: self.title, self.author, self.publication_year>, <Book: Book: self.title, self.author, self.publication_year>]>