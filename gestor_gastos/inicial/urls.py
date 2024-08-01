from django.urls import path
from . import views

urlpatterns = [
    path('inicial/', views.inicial, name='inicial'),
]