from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.adicionar_foco, name='adicionar_foco'),
]