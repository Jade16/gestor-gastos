from django.urls import path
from . import views

urlpatterns = [
	path('gastos/', views.listar_gastos, name='listar_gastos'),
    path('criar_gasto/', views.gastos, name='criar_gasto'),
]