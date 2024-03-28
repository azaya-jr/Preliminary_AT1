from django.urls import path
from . import views

urlpatterns = [
    path('create_deck/', views.create_deck, name='create_deck'),
    # Add more paths for other views if needed
]
