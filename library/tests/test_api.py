import json
from rest_framework import status
from django.test import TestCase, Client
from ..models import Author, Book
from ..serializers import AuthorSerializer, BookSerializer
from .generics import generic_setUp
from django.contrib.auth import get_user_model

# Inicialize the API
client = Client()

class AuthorAPITest(TestCase):
    def setUp(self):
        generic_setUp([Author(name='API TEST 1'), Author(name='API TEST 2')])
        User = get_user_model()
        user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
        client.login(username='temporary', password='temporary')

    def test_get_all(self):
        """
        Tests if the API's responses are equals to the DB data.
        """
        response = client.get(f'/v1/authors/')
        db_data = Author.objects.all()
        serialized_data = AuthorSerializer(db_data, many=True)
        self.assertEqual(response.data['results'], serialized_data.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_by_id(self):
        """
        Tests the API's getting by id
        """
        response = client.get(f'/v1/authors/1/')
        db_data = Author.objects.get(pk=1)
        serialized_data = AuthorSerializer(db_data)
        self.assertEqual(response.data, serialized_data.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # This test return error
        response = client.get(f'/v1/authors/999/')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_get_by_filter(self):
        """
        Tests the API's getting by filter
        """
        response = client.get(f'/v1/authors/?name=1')
        db_data = Author.objects.get(pk=1)
        serialized_data = AuthorSerializer([db_data], many=True)
        self.assertEqual(response.data['results'], serialized_data.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
