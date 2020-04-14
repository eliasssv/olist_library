from django.db.models import ObjectDoesNotExist
from django.contrib.auth import get_user_model
from rest_framework import status
import json
from rest_framework.request import Request
from rest_framework.test import APIRequestFactory
 
request = APIRequestFactory().get('/')
default_serializer_context = {
    'request': Request(request),
}

### GENERICS METHODS TO TESTS ### 

def api_setUp(client, objects_to_create):
    """
    Generic setUp
    \n@param client : django.test.Client
    \n@param objects_to_create : List of objects to save in database
    \n@since 2020-04-13
    \n@author eliasssv
    """
    for obj in objects_to_create:
        obj.save()
    
    User = get_user_model()
    user = User.objects.create_user('temporary', 'temporary@gmail.com', 'temporary')
    client.login(username='temporary', password='temporary')

def get_all(self, client, endpoint, model, serializer, serializer_context=None):
    """
    Generic Get All
    \n@param client : django.test.Client (authenticated)
    \n@param endpoint : endpoint URL
    \n@param model : Class of the model
    \n@param serializer : Class of the serializer
    \n@param serializer_context : context of the serializer - default = this API
    \n@since 2020-04-13
    \n@author eliasssv
    """
    response = client.get(endpoint)
    db_data = model.objects.all()
    serialized_data = serializer(db_data, many=True, context=default_serializer_context)
    self.assertEqual(response.data['results'], serialized_data.data, )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

def get_by_id(self, client, endpoint, id, model, serializer):
    """
    Generic Get by Id
    \n@param client : django.test.Client (authenticated)
    \n@param endpoint : endpoint URL
    \n@param id : object Id
    \n@param model : Class of the model
    \n@param serializer : Class of the serializer
    \n@param serializer_context : context of the serializer - default = this API
    \n@since 2020-04-13
    \n@author eliasssv
    """
    response = client.get(f'{endpoint}{id}/')
    db_data = model.objects.get(pk=1)
    serialized_data = serializer(db_data, context=default_serializer_context)
    self.assertEqual(response.data, serialized_data.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

def get_by_filter(self, client, endpoint, filter, model, serializer, compare_objects):
    """
    Generic Get by Id
    \n@param client : django.test.Client (authenticated)
    \n@param endpoint : endpoint URL
    \n@param filter : query filter
    \n@param model : Class of the model
    \n@param serializer : Class of the serializer
    \n@param compare_objects : List of objects to compare with the API response
    \n@param serializer_context : context of the serializer - default = this API
    \n@since 2020-04-13
    \n@author eliasssv
    """
    response = client.get(f'{endpoint}?{filter}')
    serialized_data = serializer(compare_objects, many=True, context=default_serializer_context)
    self.assertEqual(response.data['results'], serialized_data.data)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

def get_404(self, client, endpoint, id):
    """
    Generic Get by ID returning 404 - Not Found
    \n@param client : django.test.Client (authenticated)
    \n@param endpoint : endpoint URL
    \n@param id : object Id
    \n@since 2020-04-13
    \n@author eliasssv
    """
    response = client.get(f'{endpoint}{id}/')
    self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

def get_empty(self, client, endpoint, filter):
    """
    Generic Get by ID returning 404 - Not Found
    \n@param client : django.test.Client (authenticated)
    \n@param endpoint : endpoint URL
    \n@param filter : query filter
    \n@since 2020-04-13
    \n@author eliasssv
    """
    response = client.get(f'{endpoint}?{filter}')
    self.assertEqual(response.data['count'], 0)
    self.assertEqual(response.status_code, status.HTTP_200_OK)

def post_valid(self, client, endpoint, json_to_post):
    """
    Generic valid Post 
    \n@param client : django.test.Client (authenticated)
    \n@param endpoint : endpoint URL
    \n@param json_to_post : dictionary that will be post
    \n@since 2020-04-13
    \n@author eliasssv
    """
    response = client.post(
        endpoint,
        data=json.dumps(json_to_post),
        content_type='application/json'
    )
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)

def post_invalid(self, client, endpoint, json_to_post):
    """
    Generic valid Post 
    \n@param client : django.test.Client (authenticated)
    \n@param endpoint : endpoint URL
    \n@param json_to_post : dictionary that will be post
    \n@since 2020-04-13
    \n@author eliasssv
    """
    response = client.post(
        endpoint,
        data=json.dumps(json_to_post),
        content_type='application/json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

def put_valid(self, client, endpoint, id, json_to_post):
    """
    Generic valid Put 
    \n@param client : django.test.Client (authenticated)
    \n@param endpoint : endpoint URL
    \n@param id : object Id
    \n@param json_to_post : dictionary that will be post
    \n@since 2020-04-13
    \n@author eliasssv
    """
    response = client.put(
        f'{endpoint}{id}/',
        data=json.dumps(json_to_post),
        content_type='application/json'
    )
    self.assertEqual(response.status_code, status.HTTP_200_OK)

def put_invalid(self, client, endpoint, id, json_to_post):
    """
    Generic valid Put 
    \n@param client : django.test.Client (authenticated)
    \n@param endpoint : endpoint URL
    \n@param id : object Id
    \n@param json_to_post : dictionary that will be post
    \n@since 2020-04-13
    \n@author eliasssv
    """
    response = client.put(
        f'{endpoint}{id}/',
        data=json.dumps(json_to_post),
        content_type='application/json'
    )
    self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


def delete_valid(self, client, endpoint, id):
    """
    Generic valid Delete 
    \n@param client : django.test.Client (authenticated)
    \n@param endpoint : endpoint URL
    \n@param id : object Id
    \n@since 2020-04-13
    \n@author eliasssv
    """
    response = client.delete(
        f'{endpoint}{id}/'
    )
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

