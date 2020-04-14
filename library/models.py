from django.db import models

class Author(models.Model):
    """
    Model of Author
    \n@since 2020-04-08
    \n@author eliasssv
    """
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model of Book
    \n@since 2020-04-08
    \n@author eliasssv
    """
    name = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    edition = models.IntegerField()
    authors = models.ManyToManyField(Author, related_name="books") 

    def __str__(self):
        return self.name