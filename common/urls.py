from django.urls import path
from . import views

app_name = 'common'

urlpatterns = [
    path('', views.home, name='home'),  # Home page
    path('login/', views.login, name='login'),  # Login page
    path('register/', views.register, name='register'),  # Register page
]
