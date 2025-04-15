"""
URL configuration for librarysys project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# Import necessary modules from Django for handling admin and URL routing
from django.contrib import admin  # Import Django's admin module for admin site functionality
from django.urls import path, include  # Import path and include functions to define URL routes

# Define the URL patterns for the project
urlpatterns = [
    # This route maps the URL 'admin/' to Django's admin site
    path('admin/', admin.site.urls),  # Access the admin site at the 'admin/' URL
    
    # This route includes the URL patterns from the 'bookmap' app
    # All URLs in 'bookmap.urls' will be available at the root of the project ('')
    path('', include('bookmap.urls')),  # All other URLs are routed through the 'bookmap' app's URL configuration
]

