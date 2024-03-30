from django.urls import path
from .views import history_view  # Import the history_view function

urlpatterns = [
    path('history/', history_view, name='history'),
    # Add other URLs as needed
]