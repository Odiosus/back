from django.db import models
from rest_framework import generics, permissions, viewsets
from django_filters.rest_framework import DjangoFilterBackend

from .models import *
from .serializers import (
    BookListSerializer,
    BookDetailSerializer,
    ReviewCreateSerializer,
    CreateRatingSerializer,
    AuthorListSerializer,
)
from .service import get_client_ip


class BookViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод списка книг и одной книги"""
    filter_backends = (DjangoFilterBackend,)

    def get_queryset(self):
        movies = Book.objects.filter(draft=False).annotate(
            rating_user=models.Count("ratings",
                                     filter=models.Q(ratings__ip=get_client_ip(self.request)))
        ).annotate(
            middle_star=models.Sum(models.F('ratings__star')) / models.Count(models.F('ratings'))
        )
        return movies

    def get_serializer_class(self):
        if self.action == 'list':
            return BookListSerializer
        elif self.action == "retrieve":
            return BookDetailSerializer


class ReviewCreateViewSet(viewsets.ModelViewSet):
    """Добавление отзыва к книге"""
    serializer_class = ReviewCreateSerializer


class AddStarRatingViewSet(viewsets.ModelViewSet):
    """Добавление рейтинга книге"""
    serializer_class = CreateRatingSerializer

    def perform_create(self, serializer):
        serializer.save(ip=get_client_ip(self.request))


class AuthorViewSet(viewsets.ReadOnlyModelViewSet):
    """Вывод авторов"""
    queryset = Author.objects.all()
    serializer_class = AuthorListSerializer
