from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Review
from .serializers import ReviewSerializer
from .services import ReviewService


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
