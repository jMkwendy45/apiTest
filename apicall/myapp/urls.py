from django.urls import path
from . import views

urlpatterns = [
    path('users/', views.users),
    path('qoute/<int:page_number>/', views.quote),

  
]