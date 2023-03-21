from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.constraints import UniqueConstraint

# Create your models here.


class User(AbstractUser):
    pass


class Book(models.Model):
    CHOICES = (
        ('education', 'Education'),
        ('graphic novel', 'Graphic Novel'),
        ('horror', 'Horror'),
        ('romance', 'Romance'),
        ('thriller', 'Thriller'),
    )

    title = models.CharField(max_length=100)
    author = models.ForeignKey(
        to='Author',
        on_delete=models.CASCADE,
    )
    date_published = models.DateField(blank=True, null=True)
    genre = models.CharField(choices=CHOICES, max_length=50)
    featured = models.BooleanField(default=False)

    class Meta:
        constraints = [
            UniqueConstraint(fields=['author', 'title'],
                             name='unique_constraint')
        ]


class Author(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
