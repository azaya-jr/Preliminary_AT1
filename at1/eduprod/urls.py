from django.urls import path
from . import views

urlpatterns = [
    path('', views.my_view, name='my_view'),  # This is the homepage URL
    path('process_data/', views.process_data, name='process_data'),  # This is the URL for processing data
    path('handle_action/', views.handle_action, name='handle_action'),
    path('handle-answer/<str:answer>/', views.handle_answer, name='handle_answer'),
]
