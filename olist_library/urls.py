from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from library import apis

router = routers.DefaultRouter()
router.register(r'authors', apis.AuthorViewSet)
router.register(r'books', apis.BookViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
