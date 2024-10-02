from django.urls import path
from . import views


urlpatterns = [
    path('room/', views.room_list, name='room_list'),
    path('room/create/', views.create_room, name='create_room'),
    path('room/detail/<int:room_id>', views.room_detail, name='room_detail'),
    path('room/update/<int:room_id>/', views.update_room, name='update_room'),
    path('room/delete/<int:room_id>', views.delete_room, name='delete_room'),
    path('room/availability/<int:room_id>/', views.room_availability, name='room_availability'),
    path('room/events/<int:room_id>/', views.event_room_availability, name='room_event'),
]