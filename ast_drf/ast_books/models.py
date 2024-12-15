from django.db import models


class Book(models.Model):
    """Книги"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    author = models.CharField("Автор", max_length=100)
    video_url = models.URLField("Ссылка на видео", blank=True, null=True, help_text="Ссылка на видео книги")
    price_url = models.URLField("Ссылка на покупку", blank=True, null=True, help_text="Ссылка на покупку книги")
    motion_object = models.FileField("Файл движения (3D-объект)", upload_to="motion_object/", blank=True, null=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class BookPicture(models.Model):
    """Картинки страниц книг"""
    title = models.CharField("Название", max_length=100, blank=True, null=True)
    image = models.ImageField("Изображение", upload_to="book_picture/")
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Фото страниц книги"
        verbose_name_plural = "Фото страниц книги"


class Review(models.Model):
    """Отзывы"""
    author = models.CharField(max_length=255, verbose_name="Автор")
    create = models.DateTimeField(verbose_name="Дата отзыва")
    text = models.TextField(verbose_name="Текст отзыва")
    pros = models.TextField(verbose_name="Плюсы")

    def __str__(self):
        return f"{self.author} - {self.create}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"


class ReviewPicture(models.Model):
    """Картинки отзывов"""
    title = models.CharField("Название", max_length=100, blank=True, null=True)
    image = models.ImageField("Изображение", upload_to="review_picture/")
    review = models.ForeignKey(Review, verbose_name="Отзыв", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Картинка отзыва"
        verbose_name_plural = "Картинки отзывов"