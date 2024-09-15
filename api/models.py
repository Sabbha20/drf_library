from django.db import models
import uuid
# Create your models here.

class Book(models.Model):
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    authors = models.ManyToManyField('Author', related_name='books')
    isbn = models.CharField(max_length=13, null=True, blank=True, unique=True)
    isbn13 = models.CharField(max_length=13, null=True, blank=True, unique=True)
    asin = models.CharField(max_length=10, null=True, blank=True, unique=True)
    language = models.CharField(max_length=50, null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)
    rating_dist = models.CharField(max_length=255, null=True, blank=True)
    ratings_count = models.IntegerField(null=True, blank=True)
    text_reviews_count = models.IntegerField(null=True, blank=True)
    publication_date = models.DateField(null=True, blank=True)
    original_publication_date = models.DateField(null=True, blank=True)
    format = models.CharField(max_length=50, null=True, blank=True)
    edition_information = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    publisher = models.CharField(max_length=255, null=True, blank=True)
    num_pages = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    series = models.ForeignKey('Series', null=True, blank=True, on_delete=models.SET_NULL, related_name='books')

    def __str__(self):
        return self.title
    
class Author(models.Model):
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    gender = models.CharField(max_length=20, null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    about = models.TextField(null=True, blank=True)
    fans_count = models.IntegerField(null=True, blank=True)
    ratings_count = models.IntegerField(null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)
    text_reviews_count = models.IntegerField(null=True, blank=True)
    works_count = models.IntegerField(null=True, blank=True)
    work_ids = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name
    
class Series(models.Model):
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    title = models.CharField(max_length=255)
    description = models.TextField(null=True, blank=True)
    note = models.TextField(null=True, blank=True)
    series_works_count = models.IntegerField(null=True, blank=True)
    primary_work_count = models.IntegerField(null=True, blank=True)
    numbered = models.BooleanField(default=False)
    works = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class List(models.Model):
    id = models.CharField(max_length=100, primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=255)
    about = models.TextField(null=True, blank=True)
    image_url = models.URLField(null=True, blank=True)
    ratings_count = models.IntegerField(null=True, blank=True)
    average_rating = models.FloatField(null=True, blank=True)
    text_reviews_count = models.IntegerField(null=True, blank=True)
    work_ids = models.TextField(null=True, blank=True)
    book_ids = models.TextField(null=True, blank=True)
    works_count = models.IntegerField(null=True, blank=True)
    fans_count = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=20, null=True, blank=True)
    books = models.ManyToManyField('Book', related_name='lists', blank=True)
    authors = models.ManyToManyField('Author', related_name='lists', blank=True)

    def __str__(self):
        return self.name