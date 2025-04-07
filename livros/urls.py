from django.urls import path
from . import views


urlpatterns = [
    path('', views.listar_livros, name= 'listar_livros'),
    path('api/livros/', views.read_livros),
    path('criar/', views.create_livros),
]