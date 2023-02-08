

from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('students/<uuid:pk>/', views.student_detail, name='student-detail'),
    path('about/', views.about, name='about'),
]
