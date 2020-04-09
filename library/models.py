from django.db import models

class Author(models.Model):
    """
    Model of Author
    @since 2020-04-08
    @author eliasssv
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Model of Book
    @since 2020-04-08
    @author eliasssv
    """
    name = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    edition = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, related_name="books") 

    def __str__(self):
        return self.name