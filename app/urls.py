from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('', include('user.urls')),
    path('', include('room.urls')),
    path('', include('reserve.urls')),
    path('', include('equipment.urls')),
]
