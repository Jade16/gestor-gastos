from django.urls import path
from . import views

urlpatterns = [
	path('recebimentos/', views.listar_recebimentos, name='listar_recebimentos'),
    path('criar_recebimento/', views.recebimentos, name='criar_recebimento'),
]