from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

class ServiceRequest(models.Model):
    REQUEST_TYPES = [
        ('Gas Leakage', 'Gas Leakage'),
        ('Meter Issue', 'Meter Issue'),
        ('Billing Issue', 'Billing Issue'),
    ]

    STATUS_CHOICES = [
        ('Pending', 'Pending'),
        ('In Progress', 'In Progress'),
        ('Resolved', 'Resolved'),
    ]

    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name='support_servicerequests',  # Unique related_name for support ServiceRequest
    )
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES, db_index=True)
    description = models.TextField()
    file_attachment = models.FileField(upload_to='service_requests/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending', db_index=True)
    created_at = models.DateTimeField(auto_now_add=True)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} - {self.request_type} - {self.status}"

    def resolve(self, resolution_time=None):
        """Mark the service request as resolved."""
        self.status = 'Resolved'
        self.resolved_at = resolution_time or timezone.now()
        self.save()

    def is_resolved(self):
        """Check if the request is resolved."""
        return self.status == 'Resolved'
