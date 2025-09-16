from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('request-ride/', views.request_ride, name='request_ride'),
    path('accept-ride/<int:ride_id>/', views.accept_ride, name='accept_ride'),
]
