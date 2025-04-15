from django.urls import path, include  # Import path and include for URL patterns
from .views import *  # Import all views from current app

from rest_framework.routers import DefaultRouter  # Import DRF's router for ViewSets

# Create a default router instance
router = DefaultRouter()
# Register the BookViewSet at the 'books' endpoint
router.register(r'books', BookViewSet, basename='book')

urlpatterns = [
    path('', IndexView.as_view(), name='index'),  # Home page view
    path('signup/', SignUpView.as_view(), name='signup'),  # Signup logic (API)
    path('signin-page/', SignInPageView.as_view(), name='signin_page'),  # Signin page (HTML)
    path('signup-page/', SignUpPageView.as_view(), name='signup_page'),  # Signup page (HTML)
    path('api/signin/', SignInAPI.as_view(), name='api-signin'),  # Signin logic (API)
    path('admin-portal/', AdminPortalView.as_view(), name='admin_portal'),  # Admin dashboard (HTML)
    
    path('api/', include(router.urls)),  # Include all routes from the registered router
    path('api-auth/', include('rest_framework.urls')),  # Browsable API login/logout
    
    path('edit-book/', edit_book_view, name='edit_book'),  # HTML page for editing a book
    
    # Custom route for PATCH and DELETE methods on a specific book
    path(
        'api/books/<int:pk>/',
        BookViewSet.as_view({'patch': 'partial_update', 'delete': 'destroy'}),
        name='book_update_delete'
    ),

    path('student-view/', StudentView.as_view(), name='student-view'),  # View for student-facing page
]
