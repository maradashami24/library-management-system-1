# Import necessary classes and modules for Django REST API and templates
from rest_framework import status                     # HTTP status codes
from rest_framework.response import Response          # To send response objects
from rest_framework.views import APIView              # Base class for creating custom API views
from django.contrib.auth.models import User           # Django built-in User model
from rest_framework.authtoken.models import Token     # Token model for token-based authentication
from django.contrib.auth import authenticate          # Function to authenticate user credentials
from rest_framework import viewsets                   # For model viewsets to handle CRUD
from rest_framework.permissions import IsAuthenticated  # Ensures only authenticated users access certain views
from .models import Book                              # Import the Book model
from .serializers import BookSerializer               # Import the serializer for Book model
from django.views.generic import TemplateView         # For rendering HTML templates
from django.shortcuts import render                   # To render templates from function-based views

# API to handle user signup logic
class SignUpView(APIView):
    def post(self, request, *args, **kwargs):
        email = request.data.get('email')             # Extract email from request
        password = request.data.get('password')       # Extract password from request
        
        if not email or not password:                 # Validate if both fields are present
            return Response({"error": "Email and Password are required"}, status=status.HTTP_400_BAD_REQUEST)

        # Check if user already exists with the given email
        if User.objects.filter(email=email).exists():
            return Response({"error": "Email already exists"}, status=status.HTTP_400_BAD_REQUEST)
        
        # Create a new user with email as both username and email
        user = User.objects.create_user(username=email, email=email, password=password)
        
        # Generate a token for the new user
        token, created = Token.objects.get_or_create(user=user)

        # Return token and success message
        return Response({
            "message": "User created successfully",
            "token": token.key
        }, status=status.HTTP_201_CREATED)

# API to handle user sign-in (authentication) and return token
class SignInAPI(APIView):
    def post(self, request):
        email = request.data.get('email')             # Extract email
        password = request.data.get('password')       # Extract password

        user = authenticate(request, username=email, password=password)  # Validate credentials
        if user is not None:
            token, created = Token.objects.get_or_create(user=user)      # Get or create token
            return Response({'message': 'Login successful', 'token': token.key})  # Send token
        return Response({'error': 'Invalid credentials'}, status=400)    # Invalid login response

# HTML page view for sign-up form
class SignUpPageView(TemplateView):
    template_name = 'sign_up.html'                     # Template for sign-up

# HTML page view for sign-in form
class SignInPageView(TemplateView):
    template_name = 'sign_in.html'                     # Template for sign-in

# Admin portal page view
class AdminPortalView(TemplateView):
    template_name = 'admin_portal.html'                # Template for admin dashboard

# Book API endpoints for CRUD (Create, Read, Update, Delete) with auth protection
class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()                      # All book records
    serializer_class = BookSerializer                  # Book serializer
    permission_classes = [IsAuthenticated]             # Only allow authenticated access

    # Custom update method (PATCH)
    def update(self, request, *args, **kwargs):
        book = self.get_object()                       # Get the book object
        serializer = self.get_serializer(book, data=request.data, partial=True)  # Partial update allowed
    
        if serializer.is_valid():                      # Check if data is valid
            serializer.save()                          # Save updated book
            return Response({
                'message': 'Book updated successfully!',
                'book': serializer.data
            }, status=status.HTTP_200_OK)
    
        # If invalid, return error message and details
        return Response({
            'error': 'Failed to update the book. Please check the provided data.',
            'details': serializer.errors
        }, status=status.HTTP_400_BAD_REQUEST)

    # Custom delete method
    def destroy(self, request, *args, **kwargs):
        book = self.get_object()                       # Get the book object
        book.delete()                                  # Delete the book

        # Return custom success response
        return Response({
            'message': 'Book deleted successfully!'
        }, status=status.HTTP_204_NO_CONTENT)

# Function-based view to render edit book page (for frontend UI)
def edit_book_view(request):
    return render(request, 'edit_book.html')           # Render edit_book.html template

# HTML page for student view (view-only access to books)
class StudentView(TemplateView):
    template_name = 'student_view.html'                # Template for student book view

# Index/home page of the app
class IndexView(TemplateView):
    template_name = 'index.html'                       # Template for homepage
