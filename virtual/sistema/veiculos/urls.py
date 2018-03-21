from django.urls import path

from . import views

urlpatterns = [
    path('', views.VeiculosList.as_view(), name='listar-veiculos'),
]