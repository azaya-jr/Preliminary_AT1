from django.urls import path
from . import views

urlpatterns = [
    path('flash-card-roulette/', views.flash_card_roulette, name='flash_card_roulette'),
    # Add other URL patterns here if needed
]
