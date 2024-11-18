from django.db import models
from django.contrib.auth.models import User

class LogEntry(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="log_entries")
    message = models.TextField()
    level = models.CharField(
        max_length=10,
        choices=[
            ('INFO', 'INFO'),
            ('WARNING', 'WARNING'),
            ('ERROR', 'ERROR'),
        ]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Log entry ({self.level}) at {self.created_at} by {self.user.username}"
