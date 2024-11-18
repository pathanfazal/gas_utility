from django.urls import path
from . import views

urlpatterns = [
    path('', views.log_list, name='log_list'),  # List logs
    path('<int:log_id>/', views.log_detail, name='log_detail'),  # Log detail
    path('generate/', views.generate_log, name='generate_log'),  # Trigger async log creation
]
