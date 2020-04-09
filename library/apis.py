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