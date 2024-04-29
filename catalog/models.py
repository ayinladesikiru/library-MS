from uuid import uuid4
from django.db import models
from django.conf import settings
from .validators import validate_file_size


class Author(models.Model):
    first_name = models.CharField(max_length=255, null=True,
                                  blank=True, default="", help_text='Enter your name')
    last_name = models.CharField(max_length=255)
    date_of_birth = models.DateField(null=True, blank=True)
    date_of_death = models.DateField(blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Genre(models.Model):
    name = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.name}'


class Book(models.Model):
    title = models.CharField(max_length=255)
    summary = models.TextField()
    isbn = models.CharField(max_length=13)
    genre = models.ManyToManyField(Genre)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title}"

    def list_genre(self):
        return ', '.join(genre.name for genre in self.genre.all())


class BookImage(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='book_images')
    image = models.ImageField(upload_to='catalog/images',
                              validators=[validate_file_size])


class Language(models.Model):
    name = models.CharField(max_length=255)


class BookInstance(models.Model):
    AVAILABLE = 'A'
    UNAVAILABLE = 'U'
    STATUS_CHOICES = [
        (AVAILABLE, 'Available'),
        (UNAVAILABLE, 'Unavailable'),
    ]
    unique_id = models.UUIDField(default=uuid4, primary_key=True)
    due_back = models.DateTimeField()
    status = models.CharField(max_length=1, choices=STATUS_CHOICES, default=AVAILABLE)
    book = models.ForeignKey(Book, on_delete=models.PROTECT)
    borrower = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.PROTECT)


class Review(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
