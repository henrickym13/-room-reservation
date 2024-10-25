from django.urls import path
from . import views


urlpatterns = [
    path('report/', views.usage_report, name='usage_report'),
    path('report/pdf/', views.render_pdf_view, name='exportar_relatorio_completo'),
]