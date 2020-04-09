from django.contrib import admin
from .models import Author, Book

## Models registration on /admin
admin.site.register(Author)
admin.site.register(Book)
