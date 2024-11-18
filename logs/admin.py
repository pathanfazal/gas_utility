from django.contrib import admin
from .models import LogEntry

@admin.register(LogEntry)
class LogEntryAdmin(admin.ModelAdmin):
    list_display = ('user', 'message', 'level', 'created_at')
    list_filter = ('level', 'created_at')
    search_fields = ('user__username', 'message')
