from django.urls import path
from . import views


urlpatterns = [
    path('reserve/', views.reserve_list, name='reserve_list'),
    path('reserve/create/', views.reserve_create, name='reserve_create'),
]