from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    pass


class Book(models.Model):
    CHOICES = (
        ('', ''),
        ('art', 'Art'),
        ('biography', 'Biography'),
        ('business', 'Business'),
        ('classics', 'Classics'),
        ('dystopian fiction', 'Dystopian Fiction'),
        ('education', 'Education'),
        ('fantasy', 'Fantasy'),
        ('graphic novel', 'Graphic Novel'),
        ('history', 'History'),
        ('horror', 'Horror'),
        ('kids lit', 'Kids Lit'),
        ('mystery', 'Mystery'),
        ('philosophy', 'Philosophy'),
        ('politics', 'Politics'),
        ('religion', 'Religion'),
        ('romance', 'Romance'),
        ('sci-fi', 'Sci-Fi'),
        ('thriller', 'Thriller'),
        ('other', 'Other'),
    )

    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
    )
    year_published = models.PositiveIntegerField(blank=True, null=True)
    genre = models.CharField(choices=CHOICES, max_length=100)
    blurb = models.TextField(max_length=2000, blank=True, null=True)
    featured = models.BooleanField(default=False)

    class Meta:
        ordering = ['title']
        constraints = [
            models.UniqueConstraint(
                fields=['author', 'title'],
                name='book_constraint'),
        ]

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=2000, blank=True, null=True)

    class Meta:
        ordering = ['name']
        constraints = [
            models.UniqueConstraint(
                fields=['name'],
                name='author_constraint'),
        ]

    def __str__(self):
        return self.name


class Tracker(models.Model):
    CHOICES = (
        ('want to read', 'Want to Read'),
        ('reading', 'Reading'),
        ('finished', 'Finished'),
    )

    user = models.ForeignKey(
        to='User',
        on_delete=models.CASCADE,
        related_name='tracker_instances'
    )
    book = models.ForeignKey(
        to='Book',
        on_delete=models.CASCADE,
        related_name='tracker_instances'
    )
    status = models.CharField(choices=CHOICES, max_length=100)

    class Meta:

        constraints = [
            models.UniqueConstraint(fields=['user', 'book'],
                                    name='tracker_constraint')
        ]

    def __str__(self):
        return f'{self.user.username} -- {self.book.title} -- {self.status}'


# class Notes(models.Model):
#     pass
