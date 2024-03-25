from django.urls import path
from .views import login

urlpatterns = [
    path('login/', login, name='login'),
    # Remove the duplicate pattern below if it exists
    # path('login/', login, name='login'),  
    # Add other URL patterns as needed
]
