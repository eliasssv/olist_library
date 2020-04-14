from rest_framework import serializers
from .models import Author, Book

class AuthorSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer of Author
    \n@since 2020-04-08
    \n@author eliasssv
    """
    class Meta:
        model = Author
        fields = ['id', 'name']

class BookSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer of Book
    \n@since 2020-04-08
    \n@author eliasssv
    """
    class Meta:
        model = Book
        fields = ['id', 'name', 'publication_year', 'edition', 'authors']   