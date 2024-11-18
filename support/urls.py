from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='support_dashboard'),  # Support dashboard
    path('manage_request/<int:request_id>/', views.manage_request, name='manage_request'),  # Manage a specific service request
    path('resolve_request/<int:request_id>/', views.resolve_request, name='resolve_request'),  # Resolve a service request
]
