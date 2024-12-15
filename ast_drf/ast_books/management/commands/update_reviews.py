from django.core.management.base import BaseCommand
from ast_books.services import ReviewService  # Замените на ваш путь к сервису


class Command(BaseCommand):
    help = 'Получение и обновление отзывов'

    def handle(self, *args, **kwargs):
        count = ReviewService.fetch_and_update_reviews()
        self.stdout.write(self.style.SUCCESS(f'Успешно обновлено {count} отзывов'))
