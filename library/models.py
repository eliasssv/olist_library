from django.db import models

class Author(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Book(models.Model):
    name = models.CharField(max_length=255)
    publication_year = models.IntegerField()
    edition = models.CharField(max_length=255)
    authors = models.ManyToManyField(Author, on_delete=models.CASCADE, related_name="books") 

    def __str__(self):
        return self.name