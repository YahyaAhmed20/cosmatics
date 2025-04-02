# about/urls.py

from django.urls import path
from . import views

app_name = 'about'

urlpatterns = [
    path('', views.about, name='about'),
    path('doctor/<int:doctor_id>/', views.doctor_detail, name='doctor_detail'),  # صفحة تفا
]