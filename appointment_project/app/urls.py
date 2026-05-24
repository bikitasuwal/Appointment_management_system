from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('insert/', views.insert, name='insert'),
    path('delete/<int:id>/', views.delete_appointment, name='delete'),
    path('edit/<int:id>/', views.edit_appointment, name='edit'),
]
