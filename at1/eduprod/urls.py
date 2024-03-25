from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='my_view'),  # This is the homepage URL
    path('process_data/', views.process_data, name='process_data'),  # This is the URL for processing data
    path('display_random_question/', views.display_random_question, name='display_random_question'),  # New URL for displaying a random question
]
