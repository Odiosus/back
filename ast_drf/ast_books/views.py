from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets
from .models import Review, Book, BookPicture
from .serializers import ReviewSerializer, BookSerializer, BookPictureSerializer
from .services import ReviewService


class BaseReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    """
    Базовый класс для ReadOnlyViewSet с универсальными ответами.
    """

    def list(self, request, *args, **kwargs):
        """
        Получение списка объектов.
        """
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )

    def retrieve(self, request, *args, **kwargs):
        """
        Получение информации о конкретном объекте.
        """
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(
            {"status": "success", "data": serializer.data},
            status=status.HTTP_200_OK
        )


class BookViewSet(BaseReadOnlyViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookPictureViewSet(BaseReadOnlyViewSet):
    queryset = BookPicture.objects.all()
    serializer_class = BookPictureSerializer


class ReviewView(APIView):
    def get(self, request):
        # Получаем все отзывы из базы данных
        reviews = Review.objects.all()
        serializer = ReviewSerializer(reviews, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request):
        # Обновляем отзывы через сервисный слой
        count = ReviewService.fetch_and_update_reviews()
        return Response(
            {"message": f"Successfully updated {count} reviews."},
            status=status.HTTP_200_OK
        )
