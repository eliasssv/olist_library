from django.test import TestCase, Client
from library.models import Author, Book
from library.serializers import BookSerializer
from .api_tests_generic import api_setUp, get_all, get_by_id, get_by_filter, get_404, get_empty, post_valid, post_invalid, put_invalid, put_valid, delete_valid

# Inicialize the API
client = Client()
endpoint = '/v1/books/'

### GET TESTS ###
class BookAPIGetTest(TestCase):

    def setUp(self):
        author_1 = Author.objects.create(name='API TEST 1')
        author_2 = Author.objects.create(name='API TEST 2')
        book_1 = Book.objects.create(
            name='API TEST 1',
            publication_year=2020,
            edition=1
        )
        book_1.authors.set([author_1, author_2])

        book_2 = Book.objects.create(
            name='API TEST 2',
            publication_year=1900,
            edition=145
        )
        book_2.authors.set([author_2])

        api_setUp(client, [book_1, book_2])
     
    def test_get_all(self):
        """
        Tests if the API's responses are equals to the DB data.
        """
        get_all(self, client, endpoint, Book, BookSerializer)
    
    def test_get_by_id(self):
        """
        Tests the API's getting by id
        """
        get_by_id(self, client, endpoint, 1, Book, BookSerializer)  
    
    def test_get_by_id_404(self):
        """
        Tests the API's getting by id returning 404 - not found
        """
        get_404(self, client, endpoint, 999)

    def test_get_by_filter(self):
        """
        Tests the API's getting by filter
        """
        get_by_filter(self, client, endpoint, 'name=1', Book, BookSerializer, [Book.objects.get(pk=1)])
    
    def test_get_by_filter_empty(self):
        """
        Tests the API's getting by filter returning empty list
        """
        get_empty(self, client, endpoint, 'name=123')


### POST TESTS ###
class BookAPIPostTest(TestCase):
    
    def setUp(self):
        api_setUp(client, [Author(name='API TEST 1')])

    def test_post_valid(self):
        """
        Tests a valid API's POST
        """
        valid_post = {
            "name" : "VALID POST NAME",
            "publication_year" : 1980,
            "edition": 1,
            "authors": ["/v1/authors/1/"]

        }
        post_valid(self, client, endpoint, valid_post)

    def test_post_invalid(self):
        """
        Tests a invalid API's POST
        """
        invalid_post = {
            "name" : "API TEST 1"
        }
        post_invalid(self, client, endpoint, invalid_post)

        invalid_post = {
            "name" : "",
            "publication_year" : 1980,
            "edition": 1,
            "authors": ["/v1/authors/1/"]
        }
        post_invalid(self, client, endpoint, invalid_post)

### PUT TESTS ###
class BookAPIPutTest(TestCase):
    
    def setUp(self):
        author_1 = Author.objects.create(name='API TEST 1')
        author_2 = Author.objects.create(name='API TEST 2')
        book_1 = Book.objects.create(
            name='API TEST 1',
            publication_year=2020,
            edition=1
        )
        book_1.authors.set([author_1, author_2])

        book_2 = Book.objects.create(
            name='API TEST 2',
            publication_year=1900,
            edition=145
        )
        book_2.authors.set([author_2])

        book_3 = Book.objects.create(
            name='API TEST 3',
            publication_year=1950,
            edition=15
        )
        book_3.authors.set([author_1])

        api_setUp(client, [book_1, book_2, book_3])

    def test_put_valid(self):
        """
        Tests a valid API's PUT
        """
        valid_put = {
            "name" : 'API TEST 1 UPDATED',
            "publication_year" : 1968,
            "edition" : 15,
            "authors" : ["/v1/authors/1/"]
        }
        put_valid(self, client, endpoint, 1, valid_put)

    def test_put_invalid(self):
        """
        Tests a invalid API's PUT
        """
        invalid_put = {
            "name" : ""
        }
        put_invalid(self, client, endpoint, 2, invalid_put)

### DELETE TESTS ###
class BookAPIDeleteTest(TestCase):
    
    def setUp(self):
        author_1 = Author.objects.create(name='API TEST 1')
        author_2 = Author.objects.create(name='API TEST 2')
        book_1 = Book.objects.create(
            name='API TEST 1',
            publication_year=2020,
            edition=1
        )
        book_1.authors.set([author_1, author_2])

        api_setUp(client, [book_1])

    def test_delete_valid(self):
        """
        Tests a valid API's DELETE
        """
        delete_valid(self, client, endpoint, 1)



    
    
  