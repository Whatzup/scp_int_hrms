from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('employees/', views.employees, name='employees'),
    path('employees/add/', views.add_employee, name='add_employee'),
    path('employees/<int:pk>/', views.employee_detail, name='employee_detail'),
    path('sites/', views.sites, name='sites'),
    path('sites/add/', views.add_site, name='add_site'),
    path('sites/<int:pk>/', views.site_detail, name='site_detail'),
    path('clients/', views.clients, name='clients'),
    path('clients/add/', views.add_client, name='add_client'),
    path('clients/<int:pk>/', views.client_detail, name='client_detail'),
    path('projects/', views.projects, name='projects'),
    path('tasks/', views.tasks, name='tasks'),
    path('<str:model_name>/<int:pk>/status/', views.update_status, name='update_status'),
    path('<str:model_name>/<int:pk>/delete/', views.delete_record, name='delete_record'),
]
