from django.urls import path
from . import views

urlpatterns = [
    path('flash-card-roulette/', views.flash_card_roulette, name='flash_card_roulette'),
    path('handle_action/', views.handle_action, name='handle_action'),
    path('handle-answer/<str:answer>/', views.handle_answer, name='handle_answer'),
    # Add other URL patterns here if needed
]
