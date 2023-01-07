from django.urls import path
from .import views

urlpatterns = [
    path('index/', views.index, name= 'index'),
    path('receita/<int:id>', views.receita, name= 'receita'),
    path('form/', views.form, name= 'form'),
]
