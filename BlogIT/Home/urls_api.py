from django.urls import path
from .views_api import *

urlpatterns = [
    path('login',LoginView.as_view(),name='login_api'),
    path('register',RegisterView.as_view(),name='register_api'),
    
]