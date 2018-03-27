from django.urls import path

from . import views

urlpatterns = [
    path('', views.VeiculosList.as_view(), name='listar-veiculos'),   
    path(r'novo/', views.VeiculosNew.as_view(), name='novo-veiculo'),
    path(r'<int:pk>/', views.VeiculosEdit.as_view(), name='editar-veiculo'),
    path(r'excluir/<int:pk>/', views.VeiculosDelete.as_view(), name='deletar-veiculo'),
]