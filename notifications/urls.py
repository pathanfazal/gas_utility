from django.urls import path
from . import views

urlpatterns = [
    path('', views.notification_list, name='notification_list'),  # List notifications
    path('<int:notification_id>/', views.notification_detail, name='notification_detail'),  # View a specific notification
]
