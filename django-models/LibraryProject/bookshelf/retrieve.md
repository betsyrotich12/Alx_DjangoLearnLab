In [7]: book = Book.objects.create(
   ...: title = "1984",
   ...: author = "George Orwell",
   ...: publication_year = 1949
   ...: )

In [8]: retrieved_book = Book.objects.get(id=book.id)

#Expected outputs

In [9]: print(retrieved_book.title)
1984

In [10]: print(retrieved_book.author)
George Orwell

In [11]: print(retrieved_book.publication_year)
1949