from django.test import TestCase, Client
from library.models import Author
from library.serializers import AuthorSerializer
from .api_tests_generic import api_setUp, get_all, get_by_id, get_by_filter, get_404, get_empty, post_valid, post_invalid, put_invalid, put_valid, delete_valid

# Inicialize the API
client = Client()
endpoint = '/v1/authors/'

### GET TESTS ###
class AuthorAPIGetTest(TestCase):

    def setUp(self):
        api_setUp(client, [Author(name='API TEST 1'), Author(name='API TEST 2')])
        
    def test_get_all(self):
        """
        Tests if the API's responses are equals to the DB data.
        """
        get_all(self, client, endpoint, Author, AuthorSerializer)

    def test_get_by_id(self):
        """
        Tests the API's getting by id
        """
        get_by_id(self, client, endpoint, 1, Author, AuthorSerializer)
    
    def test_get_by_id_404(self):
        """
        Tests the API's getting by id returning 404 - not found
        """
        get_404(self, client, endpoint, 999)

    def test_get_by_filter(self):
        """
        Tests the API's getting by filter
        """
        get_by_filter(self, client, endpoint, 'name=1', Author, AuthorSerializer, [Author.objects.get(pk=1)])
    
    def test_get_by_filter_empty(self):
        """
        Tests the API's getting by filter returning empty list
        """
        get_empty(self, client, endpoint, 'name=123')

### POST TESTS ###
class AuthorAPIPostTest(TestCase):
    
    def setUp(self):
        api_setUp(client, [Author(name='API TEST 1')])

    def test_post_valid(self):
        """
        Tests a valid API's POST
        """
        valid_post = {
            "name" : "VALID POST NAME"
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
            "name" : ""
        }
        post_invalid(self, client, endpoint, invalid_post)

### PUT TESTS ###
class AuthorAPIPutTest(TestCase):
    
    def setUp(self):
        api_setUp(client, [Author(name='API TEST 1'), Author(name='API TEST 2'), Author(name='API TEST 3')])

    def test_put_valid(self):
        """
        Tests a valid API's PUT
        """
        valid_put = {
            "name" : "VALID PUT NAME"
        }
        put_valid(self, client, endpoint, 1, valid_put)

    def test_put_invalid(self):
        """
        Tests a invalid API's PUT
        """
        invalid_put = {
            "name" : "API TEST 3"
        }
        put_invalid(self, client, endpoint, 2, invalid_put)
        invalid_put = {
            "name" : ""
        }
        put_invalid(self, client, endpoint, 2, invalid_put)


### DELETE TESTS ###
class AuthorAPIDeleteTest(TestCase):
    
    def setUp(self):
        api_setUp(client, [Author(name='API TEST 1')])

    def test_delete_valid(self):
        """
        Tests a valid API's DELETE
        """
        delete_valid(self, client, endpoint, 1)
        