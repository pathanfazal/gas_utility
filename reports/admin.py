# reports/admin.py
from django.contrib import admin
from .models import Report  # Registering report model

# Register Report model to admin for generating and viewing reports
admin.site.register(Report)
