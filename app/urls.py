from django.urls import path
from . import views

urlpatterns = [
	
	path('', views.dashboard, name = 'dashboard'),
	path('add/', views.addForm, name = 'addForm'),
	path('edit/<int:pk>/', views.editForm, name  = 'editForm'),
	
]