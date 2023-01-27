from django.urls import path
from . import views
  
urlpatterns = [
    path('hello', views.HelloView.as_view(), name ='hello'),
    path('register', views.RegistrationView.as_view(), name ='register'),
]