from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):
    notification_type = models.CharField(max_length=100)
    message = models.TextField()
    recipient = models.ForeignKey(User, on_delete=models.CASCADE, db_index=True)  # Add indexing
    is_read = models.BooleanField(default=False, db_index=True)  # Add indexing
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)  # Add indexing

    def __str__(self):
        return f"Notification for {self.recipient.username} - {self.notification_type}"
