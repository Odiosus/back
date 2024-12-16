from django.contrib import admin
from django.contrib import messages
from django.utils.safestring import mark_safe

from .models import Review, Book, BookPicture, ReviewPicture
from .services import ReviewService


# Инлайн для модели BookPicture
class BookPictureInline(admin.TabularInline):
    model = BookPicture
    extra = 1
    fields = ('title', 'image')
    readonly_fields = ("image_preview",)

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="100" height="110"')
        return 'Нет изображения'

    image_preview.short_description = "Превью"


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'description_short', 'author', 'price_url')
    search_fields = ('title', 'description')
    list_filter = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'description', 'author', 'price_url')
        }),
    )
    inlines = [BookPictureInline]

    def description_short(self, obj):
        return obj.description[:50] + '...' if len(obj.description) > 50 else obj.description

    description_short.short_description = 'Описание'


@admin.register(BookPicture)
class BookPictureAdmin(admin.ModelAdmin):
    list_display = ('book', 'image_preview', 'title')
    search_fields = ('title', 'book__title')
    list_filter = ('book',)
    fieldsets = (
        (None, {
            'fields': ('book', 'title', 'image',)
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="100" height="110"')
        return 'Нет изображения'

    image_preview.short_description = 'Превью'
    # image_preview.allow_tags = True


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
            f"Успешно обновлено {count} отзывов.",
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


@admin.register(ReviewPicture)
class ReviewPictureAdmin(admin.ModelAdmin):
    list_display = ('title', 'image_preview')
    search_fields = ('title',)
    fieldsets = (
        (None, {
            'fields': ('title', 'image')
        }),
    )

    def image_preview(self, obj):
        if obj.image:
            return mark_safe(f'<img src={obj.image.url} width="100" height="110"')
        return 'Нет изображения'

    image_preview.short_description = 'Превью'
