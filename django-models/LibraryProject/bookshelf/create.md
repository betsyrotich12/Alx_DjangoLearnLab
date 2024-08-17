#create a book instance

from django.db import models

# Create your models here.
class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    publication_year = models.IntegerField()


    def __str__(self):
        return f"Book: self.title, self.author, self.publication_year"

In [5]: book = Book.objects.create(
   ...: title = "1984",
   ...: author = "George Orwell",
   ...: publication_year = 1949
   ...: )

In [6]: print(book) # Expected output: <Book: self.title, self.author, self.publication_year>
#Output
Book: self.title, self.author, self.publication_year