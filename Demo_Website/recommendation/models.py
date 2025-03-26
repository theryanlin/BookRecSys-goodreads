from django.db import models

# Create your models here.


class WishList(models.Model):
    user_id = models.IntegerField()
    book_id = models.IntegerField()


class Book(models.Model):
    _id = models.IntegerField()
    book_id = models.IntegerField()
    books_count = models.IntegerField(default=0, blank=True)
    authors = models.TextField(default=" ", blank=True)
    original_publication_year = models.TextField(default=" ", blank=True)
    title = models.TextField(default=" ", blank=True)
    average_rating = models.TextField(default=" ", blank=True)
    image_url = models.TextField(default=" ", blank=True)
    small_image_url = models.TextField(default=" ", blank=True)


class Rank(models.Model):
    book_id = models.TextField()
    user_id = models.IntegerField()


class Rating(models.Model):
    user_id = models.IntegerField()
    book_id = models.IntegerField()
    rating = models.IntegerField()


class Genre(models.Model):
    goodreads_book_id = models.IntegerField()
    genre = models.TextField()


