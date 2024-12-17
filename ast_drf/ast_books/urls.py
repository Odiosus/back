from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import *

urlpatterns = format_suffix_patterns([
    path('reviews/', ReviewViewSet.as_view({'get': 'list'})),
    path('reviews/<int:pk>/', ReviewViewSet.as_view({'get': 'retrieve'})),
    path('reviews-picture/', ReviewPictureViewSet.as_view({'get': 'list'})),
    path('reviews-picture/<int:pk>/', ReviewPictureViewSet.as_view({'get': 'retrieve'})),
    path('books/', BookViewSet.as_view({'get': 'list'})),
    path('books/<int:pk>/', BookViewSet.as_view({'get': 'retrieve'})),
    path('books/<int:pk>/picture/', BookPictureViewSet.as_view({'get': 'list'})),
    path('books/<int:pk>/picture/<int:picture_pk>/', BookPictureViewSet.as_view({'get': 'retrieve'})),
])
