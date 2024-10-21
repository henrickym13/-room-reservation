from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('report/', views.usage_report, name='usage_report'),
    path('pdf/', views.render_pdf_view, name='exportar_relatorio_completo'),
    path('', include('user.urls')),
    path('', include('room.urls')),
    path('', include('reserve.urls')),
    path('', include('equipment.urls')),
]
