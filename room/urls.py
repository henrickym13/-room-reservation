from django.urls import path
from . import views


urlpatterns = [
    path('room/', views.room_list, name='room_list'),
    path('room/create/', views.create_room, name='create_room'),
    path('room/update/<int:room_id>/', views.update_room, name='update_room'),
    path('room/delete/<int:room_id>', views.delete_room, name='delete_room'),

    path('reserve/create/', views.create_reserve, name='reserve_create'),
    path('reserve/', views.reserve_list, name='reserve_list'),
]