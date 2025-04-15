# Import the necessary modules from the Django REST framework
from rest_framework import serializers
from .models import Book  # Import the Book model from the current app

# Define the BookSerializer class, which will be responsible for serializing and validating Book data
class BookSerializer(serializers.ModelSerializer):
    
    # Define the Meta class inside the serializer to configure the serializer behavior
    class Meta:
        model = Book  # Link the serializer to the Book model
        fields = '__all__'  # Include all fields of the Book model in the serializer

    # Define a custom validation method for the 'author' field
    def validate_author(self, value):
        # Check if the 'author' field contains any digits
        if any(char.isdigit() for char in value):
            # Raise a validation error if digits are found in the author's name
            raise serializers.ValidationError("Author name cannot contain numbers.")
        # Return the value of the author field if it passes the validation
        return value
