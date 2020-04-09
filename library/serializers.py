from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer of Author
    @since 2020-04-08
    @author eliasssv
    """
    class Meta:
        model = Author
        fields = ['id', 'name', 'books']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer of Book
    @since 2020-04-08
    @author eliasssv
    """
    class Meta:
        model = Book
        fields = ['id', 'name', 'publication_year', 'edition', 'authors']   