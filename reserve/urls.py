from django.urls import path
from . import views


urlpatterns = [
    path('reserve/', views.reserve_list, name='reserve_list'),
    path('reserve/create/', views.reserve_create, name='reserve_create'),
    path('reserve/availability/', views.seach_availability, name='seach_availability'),
    path('reserve/confirm/<int:reserve_id>/', views.confirm_reservation, name='confirm_reserve'),
    path('reserve/cancel/<int:reserve_id>/', views.cancel_reservation, name='cancel_reserve'),
    path('reserve/user/', views.my_reserves, name='my_reserves'),
]