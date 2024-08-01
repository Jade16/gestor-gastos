from django.urls import path
from . import views

urlpatterns = [
    path('configuracoes/', views.configuracoes, name='configuracoes'),
]