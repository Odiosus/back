from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from . import views

urlpatterns = format_suffix_patterns([
    path("book/", views.BookViewSet.as_view({'get': 'list'})),
    path("book/<int:pk>/", views.BookViewSet.as_view({'get': 'retrieve'})),
    path("review/", views.ReviewCreateViewSet.as_view({'post': 'create'})),
    path("rating/", views.AddStarRatingViewSet.as_view({'post': 'create'})),
    path('author/', views.AuthorViewSet.as_view({'get': 'list'})),
])
