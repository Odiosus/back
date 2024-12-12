from django.contrib import admin
from django.contrib import messages
from .models import Review
from .services import ReviewService


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('author', 'create', 'short_text', 'short_pros')
    list_filter = ('create',)
    search_fields = ('author', 'text', 'pros')
    ordering = ('-create',)

    # Определяем пользовательское действие
    actions = ['update_reviews']

    def update_reviews(self, request, queryset):
        # Вызываем метод для обновления отзывов
        count = ReviewService.fetch_and_update_reviews()

        # Уведомляем администратора о результате
        self.message_user(
            request,
            f"Successfully updated {count} reviews.",
            messages.SUCCESS
        )

    # Название действия в админ-панели
    update_reviews.short_description = "Обновить последние отзывы"

    def short_text(self, obj):
        return obj.text[:50] + '...' if len(obj.text) > 50 else obj.text

    def short_pros(self, obj):
        return obj.pros[:50] + '...' if len(obj.pros) > 50 else obj.pros

    short_text.short_description = 'Текст отзыва'
    short_pros.short_description = 'Плюсы'
