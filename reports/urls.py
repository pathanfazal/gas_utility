from django.urls import path
from . import views

urlpatterns = [
    path('', views.report_list, name='report_list'),  # View list of reports
    path('generate/', views.generate_report, name='generate_report'),  # Generate new report
    path('download/<int:report_id>/', views.download_report, name='download_report'),  # Download a report
]
