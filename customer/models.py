from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

class AccountDetails(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    account_status = models.CharField(
        max_length=20, 
        choices=[('Active', 'Active'), ('Inactive', 'Inactive')], 
        default='Active'
    )
    phone_number = models.CharField(max_length=15, unique=True)  # Ensure unique phone numbers
    address = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.account_status}"

    def clean(self):
        # Validate that phone number contains only digits
        if not self.phone_number.isdigit():
            raise ValidationError("Phone number must contain only digits.")

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
        related_name='customer_servicerequests'  # Unique related_name for customer ServiceRequest
    )
    request_type = models.CharField(max_length=50, choices=REQUEST_TYPES)
    description = models.TextField()
    file_attachment = models.FileField(upload_to='service_requests/', null=True, blank=True)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Pending')
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
