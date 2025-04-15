# Import base AppConfig class to define app-level configurations
from django.apps import AppConfig

# Define a custom AppConfig for the 'bookmap' app
class BookmapConfig(AppConfig):
    # Set the default auto-incrementing primary key field type for models in this app
    default_auto_field = 'django.db.models.BigAutoField'
    
    # Specify the name of the app this configuration belongs to
    name = 'bookmap'
