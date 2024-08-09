from django.urls import path
from . import views

urlpatterns = [
    path('contas/', views.listar_contas, name='listar_contas'),
    path('criar_conta/', views.contas, name='criar_conta')
]