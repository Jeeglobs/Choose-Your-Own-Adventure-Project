from django.contrib import admin
from .models import User, Book, Author, Tracker, FeaturedBook

# Register your models here.
admin.site.register(User)
admin.site.register(Book)
admin.site.register(Author)
admin.site.register(Tracker)
admin.site.register(FeaturedBook)
