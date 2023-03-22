from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint


class User(AbstractUser):
    pass


class Book(models.Model):
    CHOICES = (
        ('art', 'Art'),
        ('biography', 'Biography'),
        ('business', 'Business'),
        ('classics', 'Classics'),
        ('education', 'Education'),
        ('graphic novel', 'Graphic Novel'),
        ('history', 'History'),
        ('horror', 'Horror'),
        ('mystery', 'Mystery'),
        ('philosophy', 'Philosophy'),
        ('religion', 'Religion'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
    )

    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
    )
    date_published = models.DateField(blank=True, null=True)
    genre = models.CharField(choices=CHOICES, max_length=100)
    blurb = models.TextField(max_length=500, blank=True, null=True)
    featured = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(
                fields=['author', 'title'],
                name='unique_constraint'),
        ]

    def __str__(self):
        return self.title


class Author(models.Model):
    name = models.CharField(max_length=100)
    dob = models.DateField(blank=True, null=True)
    bio = models.TextField(max_length=500, blank=True, null=True)

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
    )
    book = models.ForeignKey(
        to='Book',
        on_delete=models.CASCADE,
    )
    status = models.CharField(choices=CHOICES, max_length=100)


# class Notes(models.Model):
#     pass
