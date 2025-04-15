# Importing the necessary module from Django to define models
from django.db import models  # This module is used to define database models and fields

# Define the Book model
class Book(models.Model):  # This class represents a book in the system, inheriting from Django's 'models.Model'
    
    # Define the fields for the Book model
    title = models.CharField(max_length=255)  # A CharField for the book title, with a max length of 255 characters
    author = models.CharField(max_length=255)  # A CharField for the author's name, with a max length of 255 characters
    quantity = models.PositiveIntegerField()  # A PositiveIntegerField for the quantity of books available (must be a positive integer)
    
    # Define the string representation of the Book object (used when the object is printed or displayed)
    def __str__(self):
        # Return a formatted string displaying the book title, author, and quantity
        return f"{self.title} by {self.author} (Qty: {self.quantity})"
