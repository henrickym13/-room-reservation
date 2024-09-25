from django.urls import path
from . import views


urlpatterns = [
    path('room/', views.room_list, name='room_list'),
    path('room/create/', views.create_room, name='create_room'),
    path('room/update/<int:room_id>/', views.update_room, name='update_room'),
    path('room/delete/<int:room_id>', views.delete_room, name='delete_room'),
]