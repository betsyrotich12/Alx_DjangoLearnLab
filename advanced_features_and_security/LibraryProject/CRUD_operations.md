In [5]: book = Book.objects.create(
   ...: title = "1984",
   ...: author = "George Orwell",
   ...: publication_year = 1949
   ...: )

In [6]: print(book) # Expected output: <Book: self.title, self.author, self.publication_year>
#Output
Book: self.title, self.author, self.publication_year

In [8]: retrieved_book = Book.objects.get(id=book.id)

#Expected outputs

In [9]: print(retrieved_book.title)
1984

In [10]: print(retrieved_book.author)
George Orwell

In [11]: print(retrieved_book.publication_year)
1949

In [12]: retrieved_book.title = "Nineteen Eighty-Four"

In [13]: retrieved_book.save()

In [14]: print(retrieved_book.title)
#Expected output
Nineteen Eighty-Four

# Delete retrieved books

In [15]: retrieved_book.delete()

In [17]: book = Book.objects.all()

In [18]: print(book)
#Expected output

<QuerySet [<Book: Book: self.title, self.author, self.publication_year>, <Book: Book: self.title, self.author, self.publication_year>, <Book: Book: self.title, self.author, self.publication_year>]>