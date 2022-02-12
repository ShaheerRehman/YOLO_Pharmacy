from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('emp_list/', views.EmpListView.as_view(), name='emp_list'),
    path('emp_detail/<int:pk>/', views.EmpDetailView.as_view(), name='emp_detail'),
    path('emp_delete/<int:pk>/', views.EmpDeleteView.as_view(), name='emp_delete'),
    path('emp_edit/<int:pk>/', views.EmpUpdateView.as_view(), name='emp_edit'),
    path('register/', views.register, name='register'),
    path('about/', views.AboutView.as_view(), name='about'),
]