from django.urls import path
from . import views

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('emp_list/', views.EmpListView.as_view(), name='emp_list'),
    path('emp_detail/<int:pk>/', views.EmpDetailView.as_view(), name='emp_detail'),
    path('emp_delete/<int:pk>/', views.EmpDeleteView.as_view(), name='emp_delete'),
    path('emp_edit/<int:pk>/', views.EmpUpdateView.as_view(), name='emp_edit'),
    path('register/', views.register, name='register'),
    path('comp_list/', views.CompListView.as_view(), name='comp_list'),
    path('comp_detail/<int:pk>/', views.CompDetailView.as_view(), name='comp_detail'),
    path('comp_delete/<int:pk>/', views.CompDeleteView.as_view(), name='comp_delete'),
    path('comp_edit/<int:pk>/', views.CompUpdateView.as_view(), name='comp_edit'),
    path('create/', views.CompCreateView.as_view(), name='comp_create'),
    path('create/med/', views.MedCreateView.as_view(), name='med_create'),
    path('med_detail/<int:pk>/', views.MedDetailView.as_view(), name='med_detail'),
    path('med_list/', views.MedListView.as_view(), name='med_list'),
    path('med_delete/<int:pk>/', views.MedDeleteView.as_view(), name='med_delete'),
    path('med_edit/<int:pk>/', views.MedUpdateView.as_view(), name='med_edit'),
    path('about/', views.AboutView.as_view(), name='about'),
]