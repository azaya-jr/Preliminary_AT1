from django.urls import path
from . import views

urlpatterns = [
    path('flash-card-roulette/', views.flash_card_roulette, name='flash_card_roulette'),
    path('handle-answer/<str:answer>/', views.handle_answer, name='handle_answer'),  # Add this line
    # Add other URL patterns here if needed
]
