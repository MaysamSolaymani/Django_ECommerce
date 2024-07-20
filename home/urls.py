from django.urls import path
from . import views


urlpatterns = [
    path('', views.home),
    path('newuser/', views.new_user),
]
