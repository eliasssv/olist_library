from .models import Author, Book
from rest_framework import viewsets, permissions
from .serializers import AuthorSerializer, BookSerializer


class AuthorViewSet(viewsets.ModelViewSet):
    """
    API of Author
    @since 2020-04-08
    @author eliasssv
    """
    queryset = Author.objects.all().order_by('name')
    serializer_class = AuthorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        Optionally restricts the returned list containing the name of the Author 
        @parameters: name (string)
        @since: 2020-04-08
        @author: eliasssv
        """
        name = self.request.query_params.get('name', None)
        if name is not None:
            self.queryset = self.queryset.filter(name__icontains=name)
        return self.queryset

class BookViewSet(viewsets.ModelViewSet):
    """
    API of Book
    @since 2020-04-08
    @author eliasssv
    """
    queryset = Book.objects.all().order_by('name')
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]    

    def get_queryset(self):
        """
        Optionally restricts the returned list containing the name, publication_year, edition, 
        author_name, author_id
        @parameters: name (string)
        @since: 2020-04-09
        @author: eliasssv
        """
        name = self.request.query_params.get('name', None)
        publication_year = self.request.query_params.get('publication_year', None)
        edition = self.request.query_params.get('edition', None)
        author_name = self.request.query_params.get('author_name', None)
        author_id = self.request.query_params.get('author_id', None)

        if name is not None:
            self.queryset = self.queryset.filter(name__icontains=name)

        if publication_year is not None:
            self.queryset = self.queryset.filter(publication_year=publication_year)
        
        if edition is not None:
            self.queryset = self.queryset.filter(edition__icontains=edition)
        
        if author_name is not None:
            self.queryset = self.queryset.filter(authors__name__icontains=author_name)

        if author_id is not None:
            self.queryset = self.queryset.filter(authors__id__in=author_id)
        
        return self.queryset