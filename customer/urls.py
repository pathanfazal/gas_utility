from django.urls import path
from . import views
app_name = 'customer' 
urlpatterns = [
    path('dashboard/', views.dashboard, name='dashboard'), 
    path('service_requests/', views.service_requests_list, name='service_requests_list'),  # View service requests
    path('submit_request/', views.submit_service_request, name='submit_service_request'),  # Submit a new service request
]
