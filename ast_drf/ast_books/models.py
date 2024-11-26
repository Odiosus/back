from django.db import models
from django.urls import reverse


class Author(models.Model):
    """Автор книги"""
    name = models.CharField("Имя автора", max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Автор"
        verbose_name_plural = "Авторы"


class Book(models.Model):
    """Книги"""
    title = models.CharField("Название", max_length=100)
    isbn = models.CharField("ISBN", max_length=100, default='')  # TODO вроде сейчас указывать необязательно.
    description = models.TextField("Описание")
    poster = models.ImageField("Титульная страница", upload_to="poster/")
    year = models.PositiveSmallIntegerField("Дата выхода", default=2019)
    publisher = models.CharField("Издательство", max_length=50)
    author = models.ManyToManyField(Author, verbose_name="автор", related_name="book_author")
    url = models.SlugField(max_length=130, unique=True)
    draft = models.BooleanField("Черновик", default=False)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("book_detail", kwargs={"slug": self.url})

    def get_review(self):
        return self.reviews_set.filter(parent__isnull=True)

    class Meta:
        verbose_name = "Книга"
        verbose_name_plural = "Книги"


class BookPicture(models.Model):
    """Картинки страниц книг"""
    title = models.CharField("Название", max_length=100)
    description = models.TextField("Описание")
    image = models.ImageField("Изображение", upload_to="book_picture/")
    book = models.ForeignKey(Book, verbose_name="Книга", on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Страница книги"
        verbose_name_plural = "Страницы книги"


class RatingStar(models.Model):
    """Звезда рейтинга"""
    value = models.SmallIntegerField("Значение", default=0)

    def __str__(self):
        return f'{self.value}'

    class Meta:
        verbose_name = "Звезда рейтинга"
        verbose_name_plural = "Звезды рейтинга"
        ordering = ["-value"]


class Rating(models.Model):
    """Рейтинг"""
    ip = models.CharField("IP адрес", max_length=15)
    star = models.ForeignKey(RatingStar, on_delete=models.CASCADE, verbose_name="звезда")
    movie = models.ForeignKey(
        Book,
        on_delete=models.CASCADE,
        verbose_name="книга",
        related_name="ratings"
    )

    def __str__(self):
        return f"{self.star} - {self.movie}"

    class Meta:
        verbose_name = "Рейтинг"
        verbose_name_plural = "Рейтинги"


class Review(models.Model):
    """Отзывы"""
    email = models.EmailField()
    name = models.CharField("Имя", max_length=100)
    text = models.TextField("Сообщение", max_length=5000)
    parent = models.ForeignKey(
        'self', verbose_name="Родитель", on_delete=models.SET_NULL, blank=True, null=True, related_name="children"
    )
    movie = models.ForeignKey(Book, verbose_name="фильм", on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"{self.name} - {self.movie}"

    class Meta:
        verbose_name = "Отзыв"
        verbose_name_plural = "Отзывы"
