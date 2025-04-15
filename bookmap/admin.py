# Import the necessary modules from Django
from django.contrib import admin
# Import the Book model from models.py
from .models import Book

# Register your models here.
# This makes the Book model available in the Django admin interface.
admin.site.register(Book)
