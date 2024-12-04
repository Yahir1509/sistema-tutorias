from django.urls import path
from . import views

urlpatterns = [
    path('', views.listar_solicitudes, name='listar_solicitudes'),
    path('crear/', views.crear_solicitud, name='crear_solicitud'),
]
