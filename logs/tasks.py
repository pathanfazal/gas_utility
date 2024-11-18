from .models import LogEntry

def create_log_entry(user, message, level='INFO'):
    """Create a log entry asynchronously."""
    LogEntry.objects.create(user=user, message=message, level=level)
